import logging
import os.path
import re
from pathlib import PurePath, PureWindowsPath

def split_path(path: str):
    suffix = os.path.splitext(path)[-1]
    path = path.replace("M:\\Anime\\", "")
    print(path)
    path_parts = PurePath(path).parts \
        if PurePath(path).name != path \
        else PureWindowsPath(path).parts
    path_name = path_parts[-1]
    try:
        if re.search(r"S\d{1,2}|[Ss]eason", path_parts[-2]) is not None:
            season = int(re.search(r"\d{1,2}", path_parts[-2]).group())
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

def set_folder():

    path_name, season, folder_name, suffix, download_path = split_path(r'M:\Anime\第二次被异世界召唤 (2023)\Season 1\[LoliHouse] Isekai Shoukan wa Nidome desu - 01 [WebRip 1080p HEVC-10bit AAC SRT×2].mkv')
    print(path_name)
    print(season)
    print(folder_name)
    print(suffix)
    print(download_path)

old = r'\偶像大师 灰姑\娘女孩 U149 S01E0\1.mkv'
print(old.removeprefix(os.sep))