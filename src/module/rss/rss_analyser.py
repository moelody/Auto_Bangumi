import re
import logging

from module.network import RequestContent
from module.parser import TitleParser
from module.core import DownloadClient
from module.models import BangumiData

logger = logging.getLogger(__name__)


class RSSAnalyser:
    def __init__(self):
        self._title_analyser = TitleParser()

    @staticmethod
    def find_id(bangumi_info: list[BangumiData]) -> int:
        _id = 0
        for info in bangumi_info:
            if info.id > _id:
                _id = info.id
        return _id

    def rss_to_datas(self, bangumi_info: list[BangumiData], rss_link: str) -> list[BangumiData]:
        with RequestContent() as req:
            rss_torrents = req.get_torrents(rss_link)
        # Find largest bangumi id
        _id = self.find_id(bangumi_info)
        current_info = []
        for torrent in rss_torrents:
            raw_title = torrent.name
            extra_add = True
            if bangumi_info is not []:
                for info in bangumi_info:
                    if re.search(info.title_raw, raw_title) is not None:
                        logger.debug(f"Had added {info.official_title} in auto_download rule before")
                        extra_add = False
                        current_info.append(d["title_raw"])
                        break
            if extra_add:
                _id += 1
                data = self._title_analyser.return_data(raw_title, _id)
                if data is not None:
                    current_info.append(data["title_raw"])
                    if data["official_title"] not in bangumi_info:
                        bangumi_info.append(data)
                        
        for d in bangumi_info:
            if d["title_raw"] not in current_info:
                bangumi_info.remove(d)
        return bangumi_info

    def rss_to_data(self, url, filter: bool = True) -> BangumiData:
        with RequestContent() as req:
            rss_torrents = req.get_torrents(url, filter)
        for torrent in rss_torrents:
            try:
                data = self._title_analyser.return_data(torrent.name, 9999)
                return data
            except Exception as e:
                logger.debug(e)

    def run(self, bangumi_info: list[BangumiData], download_client: DownloadClient, rss_link: str):
        logger.info("Start collecting RSS info.")
        try:
            self.rss_to_datas(bangumi_info, rss_link)
            download_client.add_rules(bangumi_info, rss_link=rss_link)
        except Exception as e:
            logger.debug(e)
        logger.info("Finished")
