from .log import setup_logger, LOG_PATH
from .config import VERSION, settings

import os
PKG_DIR = os.path.dirname(os.path.realpath(__file__))


TMDB_API = "32b19d6a05b512190a056fa4e747cbbc"
DATA_PATH = "data/data.db"

PLATFORM = "Windows" if "\\" in settings.downloader.path else "Unix"
