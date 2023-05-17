import re
import logging
import os

from module.downloader import getClient
from module.models import BangumiData, Config


from module.utils import replaceUnsafeStr

logger = logging.getLogger(__name__)


class DownloadClient:
    def __init__(self, settings: Config):
        self.client = getClient(settings)
        self.authed = False
        self.download_path = settings.downloader.path
        self.group_tag = settings.bangumi_manage.group_tag

    def auth(self):
        self.client.auth()
        self.authed = True

    def init_downloader(self):
        prefs = {
            "rss_auto_downloading_enabled": True,
            "rss_max_articles_per_feed": 500,
            "rss_processing_enabled": True,
            "rss_refresh_interval": 30,
        }
        self.client.prefs_init(prefs=prefs)
        try:
            self.client.add_category("BangumiCollection")
        except Exception as e:
            logger.warning("Cannot add new category, maybe already exists.")
            logger.debug(e)
        if self.download_path == "":
            prefs = self.client.get_app_prefs()
            self.download_path = os.path.join(prefs["save_path"], "Bangumi")

    def set_rule(self, info: BangumiData, rss_link):
        official_name, raw_name, season, group, dpi, source, subtitle = info.official_title, info.title_raw, info.season, info.group, info.dpi, info.source, info.subtitle
        rule = {
            "enable": True,
            "mustContain": raw_name,
            "mustNotContain": "|".join(info.filter),
            "useRegex": True,
            "episodeFilter": "",
            "smartFilter": False,
            "previouslyMatchedEpisodes": [],
            "affectedFeeds": [rss_link],
            "ignoreDays": 0,
            "lastMatch": "",
            "addPaused": False,
            "assignedCategory": "BangumiCollection",
            "savePath": str(
                os.path.join(
                    self.download_path,
                    re.sub(r"[:/.]", " ", official_name).strip(),
                    replaceUnsafeStr(f"[Season {season}][{group}]{raw_name}[{dpi}][{source}][{subtitle}]"),
                )
            ),
        }
        rule_name = f"[{group}] {official_name}" if self.group_tag else official_name
        self.client.rss_set_rule(rule_name=f"{rule_name} S{season}", rule_def=rule)
        logger.info(f"Add {official_name} Season {season}")

    def remove_rule(self, info: dict):
        official_name, raw_name, season, group = info["official_title"], info["title_raw"], info["season"], info["group"]
        rule_name = f"[{group}] {official_name}" if settings.bangumi_manage.group_tag else official_name
        self.client.rss_remove_rule(rule_name=f"{rule_name} S{season}")
        logger.info(f"Remove {official_name} Season {season}")

    def rss_feed(self, rss_link, item_path="Mikan_RSS"):
        # TODO: 定时刷新 RSS
        self.client.rss_add_feed(url=rss_link, item_path=item_path)

    def add_collection_feed(self, rss_link, item_path):
        self.client.rss_add_feed(url=rss_link, item_path=item_path)
        logger.info("Add Collection RSS Feed successfully.")

    def add_rules(self, bangumi_info: list[BangumiData], rss_link: str):
        logger.debug("Start adding rules.")
        for info in bangumi_info:
            if not info.added:
                self.set_rule(info, rss_link)
                info.added = True
        logger.debug("Finished.")

    def get_torrent_info(self, category="BangumiCollection"):
        return self.client.torrents_info(
            status_filter="completed", category=category
        )
    
    def get_torrent_files(self, hash):
        return self.client.torrents_files(
            hash
        )

    def rename_torrent_file(self, _hash, old_path, new_path):
        self.client.torrents_rename_file(
            torrent_hash=_hash, old_path=old_path, new_path=new_path
        )
        logger.info(f"{old_path} >> {new_path}")

    def delete_torrent(self, hashes):
        self.client.torrents_delete(
            hashes
        )
        logger.info(f"Remove bad torrents.")

    def add_torrent(self, torrent: dict, category="BangumiCollection"):
        self.client.torrents_add(
            urls=torrent["url"],
            save_path=torrent["save_path"],
            category=category
        )

    def move_torrent(self, hashes, location):
        self.client.move_torrent(
            hashes=hashes,
            new_location=location
        )

    def add_rss_feed(self, rss_link, item_path):
        self.client.rss_add_feed(url=rss_link, item_path=item_path)
        logger.info("Add RSS Feed successfully.")

    def get_download_rules(self):
        return self.client.get_download_rule()

    def get_torrent_path(self, hashes):
        return self.client.get_torrent_path(hashes)

    def set_category(self, hashes, category):
        self.client.set_category(hashes, category)

