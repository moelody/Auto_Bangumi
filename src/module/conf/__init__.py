from .log import setup_logger, LOG_PATH
from .config import settings, VERSION

import os
PKG_DIR = os.path.dirname(os.path.realpath(__file__))


TMDB_API = "32b19d6a05b512190a056fa4e747cbbc"
DATA_PATH = os.path.join(PKG_DIR, "../../data/bangumi.json")
