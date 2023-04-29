import logging
import os
import os.path
import re
from pathlib import PurePath, PureWindowsPath

PREFIX_RE = re.compile(r"[^\w\s\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff-]")
CHINESE_NUMBER_MAP = {
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "十": 10,
}

SEARCH_KEY = ["group", "official_title", "title_raw", "season_raw", "subtitle", "source", "dpi"]
TITLE_RE = re.compile(
    r"(.*|\[.*])( -? \d+|\[\d+]|\[\d+.?[vV]\d{1}]|[第]?\d+[话話集]|\[\d+.?END]|)(.*)"
)
def get_group(name: str) -> str:
    return re.split(r"[\[\]]", name)[1]
def prefix_process(raw: str, group: str) -> str:
    raw = re.sub(f".{group}.", "", raw)
    raw_process = PREFIX_RE.sub("/", raw)
    arg_group = raw_process.split("/")
    for arg in arg_group:
        if re.search(r"新番|月?番", arg) and len(arg) <= 5:
            raw = re.sub(f".{arg}.", "", raw)
        elif re.search(r"港澳台地区", arg):
            raw = re.sub(f".{arg}.", "", raw)
    return raw
def season_process(season_info: str):
    name_season = season_info
    # if re.search(r"新番|月?番", season_info):
    #     name_season = re.sub(".*新番.", "", season_info)
    #     # 去除「新番」信息
    # name_season = re.sub(r"^[^]】]*[]】]", "", name_season).strip()
    season_rule = r"S\d{1,2}|Season \d{1,2}|[第].[季期]"
    name_season = re.sub(r"[\[\]]", " ", name_season)
    seasons = re.findall(season_rule, name_season)
    if not seasons:
        return name_season, "", 1
    name = re.sub(season_rule, "", name_season)
    for season in seasons:
        season_raw = season
        if re.search(r"Season|S", season) is not None:
            season = int(re.sub(r"Season|S", "", season))
            break
        elif re.search(r"[第 ].*[季期(部分)]|部分", season) is not None:
            season_pro = re.sub(r"[第季期 ]", "", season)
            try:
                season = int(season_pro)
            except ValueError:
                season = CHINESE_NUMBER_MAP[season_pro]
                break
    return name, season_raw, season

content_title = r"[Snow-Raws] 为美好的世界献上祝福！红传说/Kono Subarashii Sekai ni Shukufuku o! Kurenai Densetsu/この素晴らしい世界に祝福を！红伝说 (BD 1920x1080 HEVC-YUV420P10 FLACx2)"

group = get_group(content_title)
match_obj = TITLE_RE.match(content_title)
season_info, episode_info, other = list(map(
                lambda x: x.strip(), match_obj.groups()
            ))
process_raw = prefix_process(content_title, group)
# 处理 前缀
raw_name, season_raw, season = season_process(process_raw)
print(process_raw)