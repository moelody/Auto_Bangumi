import logging
import os.path
import re
from pathlib import PurePath, PureWindowsPath

SEARCH_KEY = ["group", "official_title", "title_raw", "season_raw", "subtitle", "source", "dpi"]


def init_eps_complete_search_str(data: dict):
        test = [data.get(key).strip() for key in SEARCH_KEY if data.get(key) is not None]
        test[1] = re.sub(r"\s\(\d+\)$", "", test[1])
        search_str_pre = "+".join(test)
        search_str = re.sub(r"[\W_ ]", "+", search_str_pre)
        print(search_str)


init_eps_complete_search_str({
            "official_title": "为美好的世界献上爆炎！ (2023)",
            "title_raw": "为美好的世界献上爆焰！",
            "season": 1,
            "season_raw": "",
            "group": "ANi",
            "dpi": "1080P",
            "source": "Baha",
            "subtitle": "CHT",
            "added": True,
            "eps_collect": False
        })

