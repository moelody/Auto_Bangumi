import logging

from module.conf import settings
from module.models import Bangumi

from .analyser import raw_parser, tmdb_parser, torrent_parser, mikan_parser

logger = logging.getLogger(__name__)


class TitleParser:
    def __init__(self):
        pass

    @staticmethod
    def torrent_parser(
        torrent_path: str,
        torrent_name: str | None = None,
        season: int | None = None,
        file_type: str = "media",
    ):
        try:
            return torrent_parser(torrent_path, torrent_name, season, file_type)
        except Exception as e:
            logger.warning(f"Cannot parse {torrent_path} with error {e}")

    @staticmethod
    def tmdb_parser(title: str, season: int, language: str):
        tmdb_info = tmdb_parser(title, language)
        if tmdb_info:
            logger.debug(f"TMDB Matched, official title is {tmdb_info.title}")
            tmdb_season = tmdb_info.last_season if tmdb_info.last_season else season
            return tmdb_info.title, tmdb_season, tmdb_info.year, tmdb_info.poster_link
        else:
            logger.warning(f"Cannot match {title} in TMDB. Use raw title instead.")
            logger.warning("Please change bangumi info manually.")
            return title, season, None, None

    @staticmethod
    def raw_parser(raw: str) -> Bangumi | None:
        language = settings.rss_parser.language
        try:
            episode = raw_parser(raw)
            titles = {
                "zh": episode.title_zh,
                "en": episode.title_en,
                "jp": episode.title_jp,
            }
            title_raw = episode.title_en if episode.title_en else episode.title_zh
            if titles[language]:
                official_title = titles[language]
            elif titles["zh"]:
                official_title = titles["zh"]
            elif titles["en"]:
                official_title = titles["en"]
            elif titles["jp"]:
                official_title = titles["jp"]
            else:
                official_title = title_raw
            _season = episode.season
            logger.debug(f"RAW:{raw} >> {title_raw}")
            return Bangumi(
                official_title=official_title,
                title_raw=title_raw,
                season=_season,
                season_raw=episode.season_raw,
                group_name=episode.group,
                dpi=episode.resolution,
                source=episode.source,
                subtitle=episode.sub,
                eps_collect=False if episode.episode > 1 else True,
                offset=0,
                filter=",".join(settings.rss_parser.filter),
            )
        except Exception as e:
            logger.debug(e)
            logger.warning(f"Cannot parse {raw}.")
            return None

    @staticmethod
    def mikan_parser(homepage: str) -> tuple[str, str]:
        return mikan_parser(homepage)
