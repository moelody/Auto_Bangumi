import logging
import os
import os.path
import re
from pathlib import PurePath, PureWindowsPath

SEARCH_KEY = ["group", "official_title", "title_raw", "season_raw", "subtitle", "source", "dpi"]



path = "E:\Anime\鬼灭之刃 刀匠村篇 01(45)\[Season 1][豌豆字幕组&风之圣殿字幕组&LoliHouse]Kimetsu no Yaiba[1080p][WebRip][简繁外挂字幕]\[BeanSub&FZSD&LoliHouse] Kimetsu no Yaiba - 45 [WebRip 1080p HEVC-10bit AAC ASSx2].ass"

file_extension = path.split('.', 1)[-1]

print(file_extension)