import logging
import os.path
import re
import zipfile
from pathlib import PurePath, PureWindowsPath, Path

from module.core.download_client import DownloadClient

from module.conf import settings
from module.parser import TitleParser
from module.network import PostNotification, ServerChanNotification

logger = logging.getLogger(__name__)


class Renamer:
    def __init__(self, download_client: DownloadClient, bangumi_info: list):
        self.client = download_client
        self.info = bangumi_info
        self.rename_count = 0
        self._renamer = TitleParser()

    def print_result(self, torrent_count):
        if self.rename_count != 0:
            logger.info(f"Finished checking {torrent_count} files' name, renamed {self.rename_count} files.")
        logger.debug(f"Checked {torrent_count} files")

    def get_torrent_info(self):
        recent_info = self.client.get_torrent_info()
        torrent_count = len(recent_info)
        return recent_info, torrent_count

    @staticmethod
    def split_path(path: str):
        path = path.replace(settings.downloader.path, "")
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
            logger.debug(e)
            logger.debug("No Season info")
            season = 1
        folder_name = path_parts[1] if path_parts[0] == "/" else path_parts[0]
        try:
            download_path = path_parts[1]
        except IndexError:
            download_path = ""
        return path_name, season, folder_name, suffix, download_path

    def rename_torrent(self, info):
        try:
            name = info.name
            torrent_hash = info.hash
            torrent_path = info.content_path
            path_name, season, folder_name, suffix, _ = self.split_path(torrent_path)
            new_name = self._renamer.download_parser(name, folder_name, season, suffix, settings.bangumi_manage.rename_method)

            suffix = path_name.split('.', 1)[-1].replace(suffix, "")
            if (re.findall("(SC|TC)", suffix, re.I)):
                new_name = (lambda p: p[0] + "." + suffix + p[1])(os.path.splitext(new_name))
            if path_name != new_name and not zipfile.is_zipfile(torrent_path):
                logger.info(name)
                logger.info(path_name)
                logger.info(new_name)
                old_path = torrent_path.replace(info.save_path, "")
                old_path = old_path[len(os.path.sep):]
                self.client.rename_torrent_file(torrent_hash, new_name, old_path, new_name)
                self.rename_count += 1
            
        except Exception as e:
            logger.warning(f"{path_name} rename failed")
            logger.warning(f"Folder name: {folder_name}, Season: {season}, Suffix: {suffix}")
            logger.warning(e)
            if settings.bangumi_manage.remove_bad_torrent:
                self.client.delete_torrent(torrent_hash)

    def run(self):
        recent_info, torrent_count = self.get_torrent_info()
        for info in recent_info:
            torrent_path = info.content_path
            if os.path.isdir(torrent_path):
                files = self.client.get_torrent_files(info.hash)
                for file in files:
                    info.content_path = os.path.join(torrent_path, file.name)
                    self.rename_torrent(info)
                # for file in os.listdir(torrent_path):
                #     info.content_path = os.path.join(torrent_path, file)
                    # self.rename_torrent(info)
            else:
                self.rename_torrent(info)
        self.print_result(torrent_count)

    def set_folder(self):
        recent_info, _ = self.get_torrent_info()
        for info in recent_info:
            torrent_hash = info.hash
            _, season, folder_name, _, download_path = self.split_path(info.content_path)
            # new_path = os.path.join(settings.downloader.path, folder_name, f"Season {season}")
            new_path = os.path.join(settings.downloader.path, folder_name)
            # print(new_path)
            self.client.move_torrent(torrent_hash, new_path)

