from .log import setup_logger, LOG_PATH
from .config import settings, VERSION

import os
PKG_DIR = os.path.dirname(os.path.realpath(__file__))


TMDB_API = "32b19d6a05b512190a056fa4e747cbbc"
DATA_PATH = os.path.join(PKG_DIR, "../../data/bangumi.json")


class RSSLink(str):
    def __new__(cls):
        if "://" not in settings.rss_parser.custom_url:
            return f"https://{settings.rss_parser.custom_url}/RSS/MyBangumi?token={settings.rss_parser.token}"
        return f"{settings.rss_parser.custom_url}/RSS/MyBangumi?token={settings.rss_parser.token}"
