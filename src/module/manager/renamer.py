import logging
import os.path
import re
import asyncio
from pathlib import PurePath, PureWindowsPath

from module.core.download_client import DownloadClient

from module.conf import settings
from module.parser import TitleParser
from module.network import PostNotification, ServerChanNotification

logger = logging.getLogger(__name__)


class Renamer:
    def __init__(self, download_client: DownloadClient):
        self.client = download_client
        self._renamer = TitleParser()

    @staticmethod
    def print_result(torrent_count, rename_count):
        if rename_count != 0:
            logger.info(f"Finished checking {torrent_count} files' name, renamed {rename_count} files.")
        logger.debug(f"Checked {torrent_count} files")

    def get_torrent_info(self):
        recent_info = self.client.get_torrent_info()
        torrent_count = len(recent_info)
        return recent_info, torrent_count

    @staticmethod
    def split_path(path: str):
        suffix = os.path.splitext(path)[-1]
        path = path.replace(settings.downloader.path, "")
        path = path.removeprefix(os.sep)
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
            logger.debug(e)
            logger.debug("No Season info")
            season = 1
        folder_name = path_parts[1] if path_parts[0] == "/" else path_parts[0]
        try:
            download_path = path_parts[1]
        except IndexError:
            download_path = ""
        return path_name, season, folder_name, suffix, download_path

    @staticmethod
    async def delete_dir(path):
        while True:
            if os.path.isdir(path) and not os.listdir(path):
                os.rmdir(path)
                break
            await asyncio.sleep(1)

    def run(self):
        recent_info, torrent_count = self.get_torrent_info()
        rename_count = 0
        for info in recent_info:
            name = info.name
            torrent_hash = info.hash
            path_name, season, folder_name, suffix, _ = self.split_path(info.content_path)
            if path_name is folder_name:
                logger.warning("Wrong bangumi path, please check your qbittorrent settings.")
            else:
                try:
                    new_name = self._renamer.download_parser(name, folder_name, season, suffix, settings.bangumi_manage.rename_method)
                    new_path = os.path.join(settings.downloader.path, folder_name)
                    if info.save_path != new_path:
                        self.client.move_torrent(torrent_hash, new_path)
                        asyncio.run(self.delete_dir(info.save_path))
                        logger.info(f"Move {path_name} {info.save_path} << {new_path}")
                    if path_name != new_name:
                        old_path = info.content_path.replace(info.save_path, "")
                        old_path = old_path[len(os.path.sep):]
                        self.client.rename_torrent_file(torrent_hash, new_name, old_path, new_name)
                        rename_count += 1
                    else:
                        continue
                except Exception as e:
                    logger.warning(f"info: {info.content_path}")
                    logger.warning(f"name: {name}")
                    logger.warning(f"{path_name} rename failed")
                    logger.warning(f"Folder name: {folder_name}, Season: {season}, Suffix: {suffix}")
                    logger.debug(e)
                    if settings.bangumi_manage.remove_bad_torrent:
                        self.client.delete_torrent(torrent_hash)
        self.print_result(torrent_count, rename_count)

    def set_folder(self):
        recent_info, _ = self.get_torrent_info()
        for info in recent_info:
            torrent_hash = info.hash
            _, season, folder_name, _, download_path = self.split_path(info.content_path)
            # new_path = os.path.join(settings.downloader.path, folder_name, f"Season {season}")
            new_path = os.path.join(settings.downloader.path, folder_name)
            # print(new_path)
            self.client.move_torrent(torrent_hash, new_path)

