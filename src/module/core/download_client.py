import re
import logging
import os

from module.downloader import getClient

from module.conf import settings

logger = logging.getLogger(__name__)


class DownloadClient:

    unsafeStr = re.compile(r'[\u0001-\u001f\u007f-\u009f\u00ad\u0600-\u0605\u061c\u06dd\u070f\u08e2\u180e\u200b-\u200f\u202a-\u202e\u2060-\u2064\u2066-\u206f\ufdd0-\ufdef\ufeff\ufff9-\ufffb\ufffe\uffff]')
    fullWidthDict = [
        ['\\\\', '＼'],
        ['/', '／'],
        [':', '：'],
        ['\\?', '？'],
        ['"', '＂'],
        ['<', '＜'],
        ['>', '＞'],
        ['\\*', '＊'],
        ['\\|', '｜'],
        ['~', '～'],
    ]
    windowsReservedNames = [
        'CON',
        'PRN',
        'AUX',
        'NUL',
        'COM1',
        'LPT1',
        'LPT2',
        'LPT3',
        'COM2',
        'COM3',
        'COM4',
    ]

    def __init__(self):
        self.client = getClient()

    def init_downloader(self):
        prefs = {
            "rss_auto_downloading_enabled": True,
            "rss_max_articles_per_feed": 500,
            "rss_processing_enabled": True,
            "rss_refresh_interval": 30,
        }
        self.client.prefs_init(prefs=prefs)
        if settings.downloader.download_path == "":
            prefs = self.client.get_app_prefs()
            settings.downloader.path = os.path.join(prefs["save_path"], "Bangumi")

    def replaceUnsafeStr(self, str):
        for name in self.windowsReservedNames:
            if str.upper() == name:
                return str + 'UnsafeName'
        str = self.unsafeStr.sub('', str)
        # 把一些特殊字符替换成全角字符
        for index in range(len(self.fullWidthDict)):
            rule = self.fullWidthDict[index]
            reg = re.compile(rule[0])
            str = reg.sub(rule[1], str)
        return str

    def set_rule(self, info: dict, rss_link):
        official_name, raw_name, season, group, dpi, source, subtitle = info["official_title"], info["title_raw"], info["season"], info["group"], info["dpi"], info["source"], info["subtitle"]
        rule = {
            "enable": True,
            "mustContain": raw_name,
            "mustNotContain": "|".join(settings.rss_parser.filter),
            "useRegex": True,
            "episodeFilter": "",
            "smartFilter": False,
            "previouslyMatchedEpisodes": [],
            "affectedFeeds": [rss_link],
            "ignoreDays": 0,
            "lastMatch": "",
            "addPaused": settings.debug.dev_debug,
            "assignedCategory": "Bangumi",
            "savePath": str(
                os.path.join(
                    settings.downloader.path,
                    re.sub(r"[:/.]", " ", official_name).strip(),
                    self.replaceUnsafeStr(f"[{group}]{raw_name} Season {season}[{dpi}][{source}][{subtitle}]"),
                )
            ),
        }
        rule_name = f"[{group}] {official_name}" if settings.bangumi_manage.group_tag else official_name
        self.client.rss_set_rule(rule_name=f"{rule_name} S{season}", rule_def=rule)
        logger.info(f"Add {official_name} Season {season}")

    def remove_rule(self, info: dict):
        official_name, raw_name, season, group = info["official_title"], info["title_raw"], info["season"], info["group"]
        rule_name = f"[{group}] {official_name}" if settings.bangumi_manage.group_tag else official_name
        self.client.rss_remove_rule(rule_name=f"{rule_name} S{season}")
        logger.info(f"Remove {official_name} Season {season}")

    def rss_feed(self):
        # TODO: 定时刷新 RSS
        if self.client.get_rss_info() == settings.rss_parser.link:
            logger.info("RSS Already exists.")
        else:
            logger.info("No feed exists, start adding feed.")
            self.client.rss_add_feed(url=settings.rss_parser.link, item_path="Mikan_RSS")
            logger.info("Add RSS Feed successfully.")

    def add_collection_feed(self, rss_link, item_path):
        self.client.rss_add_feed(url=rss_link, item_path=item_path)
        logger.info("Add RSS Feed successfully.")

    def add_rules(self, bangumi_info, rss_link=settings.rss_parser.link):
        logger.debug("Start adding rules.")
        for info in bangumi_info:
            if not info["added"]:
                self.set_rule(info, rss_link)
                info["added"] = True
            elif settings.debug.dev_debug:
                self.remove_rule(info)
                self.set_rule(info, rss_link)
        # logger.info("to rule.")
        logger.debug("Finished.")

    def get_torrent_info(self):
        return self.client.torrents_info(
            status_filter="completed", category="Bangumi"
        )

    def rename_torrent_file(self, hash, new_file_name, old_path, new_path):
        self.client.torrents_rename_file(
            torrent_hash=hash, new_file_name=new_file_name, old_path=old_path, new_path=new_path
        )
        logger.info(f"{old_path} >> {new_path}, new name {new_file_name}")

    def delete_torrent(self, hashes):
        self.client.torrents_delete(
            hashes
        )
        logger.info(f"Remove bad torrents.")

    def add_torrent(self, torrent: dict):
        self.client.torrents_add(
            urls=torrent["url"],
            save_path=torrent["save_path"],
            category="Bangumi"
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

