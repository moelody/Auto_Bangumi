import os.path
import re
import logging

from module.conf import settings
from module.network import RequestContent

from module.core.download_client import DownloadClient

from module.utils import replaceUnsafeStr

logger = logging.getLogger(__name__)
SEARCH_KEY = ["group", "official_title", "title_raw", "season_raw", "subtitle", "source", "dpi"]


class FullSeasonGet:
    def __init__(self):
        pass

    @staticmethod
    def init_eps_complete_search_str(data: dict):
        test = [data.get(key).strip() for key in SEARCH_KEY if data.get(key) is not None]
        test[1] = re.sub(r"\s\(\d+\)", "", test[1])
        search_str_pre = "+".join(test)
        search_str = re.sub(r"[\W_ ]", "+", search_str_pre)
        return search_str

    def get_season_torrents(self, data: dict):
        keyword = self.init_eps_complete_search_str(data)
        with RequestContent() as req:
            torrents = req.get_torrents(f"https://mikanani.me/RSS/Search?searchstr={keyword}")
        return torrents

    @staticmethod
    def collect_season_torrents(data: dict, torrents):
        downloads = []
        official_name, raw_name, season, group, dpi, source, subtitle = data["official_title"], data["title_raw"], data["season"], data["group"], data["dpi"], data["source"], data["subtitle"]
        for torrent in torrents:
            download_info = {
                "url": torrent.torrent_link,
                "save_path": os.path.join(
                        settings.downloader.path,
                        official_name,
                        replaceUnsafeStr(f"[Season {season}][{group}]{raw_name}[{dpi}][{source}][{subtitle}]"),
                        )
            }
            downloads.append(download_info)
        return downloads

    def download_eps(self, data, download_client: DownloadClient):
        logger.info(f"Start collecting {data['official_title']} Season {data['season']}...")
        torrents = self.get_season_torrents(data)
        downloads = self.collect_season_torrents(data, torrents)
        for download in downloads:
            download_client.add_torrent(download)
        logger.info("Completed!")
        data["eps_collect"] = False

    def eps_complete(self, bangumi_info, download_client: DownloadClient):
        for data in bangumi_info:
            if data["eps_collect"]:
                self.download_eps(data, download_client)

    def download_collection(self, data, link, download_client: DownloadClient):
        with RequestContent() as req:
            torrents = req.get_torrents(link)
        downloads = self.collect_season_torrents(data, torrents)
        logger.info(f"Starting download {data.get('official_title')}")
        for download in downloads:
            download_client.add_torrent(download, "老番")
        logger.info("Completed!")


