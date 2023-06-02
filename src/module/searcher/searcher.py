from module.searcher.plugin import search_url
from module.network import RequestContent
from module.models import BangumiData, TorrentBase

SEARCH_KEY = [
    "group_name",
    "title_raw",
    "season_raw",
    "subtitle",
    "source",
    "dpi",
]


class SearchTorrent(RequestContent):
    def search_torrents(self, keywords: list[str], site: str = "mikan") -> list[TorrentBase]:
        url = search_url(site, keywords)
        # TorrentInfo to TorrentBase
        torrents = self.get_torrents(url)

        def to_dict():
            for torrent in torrents:
                yield {
                    "name": torrent.name,
                    "torrent_link": torrent.torrent_link,
                    "homepage": torrent.homepage,
                }
        return [TorrentBase(**d) for d in to_dict()]

    def search_season(self, data: BangumiData):
        keywords = [getattr(data, key) for key in SEARCH_KEY if getattr(data, key)]
        torrents = self.search_torrents(keywords)
        return [torrent for torrent in torrents if data.title_raw in torrent.name]


if __name__ == '__main__':
    with SearchTorrent() as st:
        for t in st.search_torrents(["魔法科高校の劣等生"]):
            print(t)