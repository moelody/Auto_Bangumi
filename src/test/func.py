import logging
import os
import os.path
import re
from pathlib import PurePath, PureWindowsPath

SEARCH_KEY = ["group", "official_title", "title_raw", "season_raw", "subtitle", "source", "dpi"]

def split_path(path: str):
    path = path.replace(r"E:\Anime", "")
    path = path.removeprefix(os.sep)
    path_parts = PurePath(path).parts \
        if PurePath(path).name != path \
        else PureWindowsPath(path).parts
    path_name = path_parts[-1]
    suffix = os.path.splitext(path_name)[1] # "." + path_name.split('.', 1)[-1] # os.path.splitext(path_name)
    try:
        if re.search(r"S\d{1,2}|[Ss]eason", path_parts[-2]) is not None:
            season = int(re.search(r"Season (\d{1,2})", path_parts[-2]).group(1))
        else:
            season = 1
    except Exception as e:
        season = 1
    folder_name = path_parts[1] if path_parts[0] == "/" else path_parts[0]
    try:
        download_path = path_parts[1]
    except IndexError:
        download_path = ""
    return path_name, season, folder_name, suffix, download_path

# path = "E:\Anime\鬼灭之刃 刀匠村篇 01(45)\[Season 1][豌豆字幕组&风之圣殿字幕组&LoliHouse]Kimetsu no Yaiba[1080p][WebRip][简繁外挂字幕]\[BeanSub&FZSD&LoliHouse] Kimetsu no Yaiba - 45 [WebRip 1080p HEVC-10bit AAC ASSx2].TC.ass"
new_name = "1.ass"
path_name = r"[WebRip 1080p HEVC-10bit AAC ASSx2].TC.ass"
suffix = "TC"
new_name = (lambda p: p[0] + "." + suffix + p[1])(os.path.splitext(new_name))
r = re.findall("(SC|TC)", suffix, re.I)

print(r)