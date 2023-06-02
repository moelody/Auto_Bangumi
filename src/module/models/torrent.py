from pydantic import BaseModel, Field


class TorrentBase(BaseModel):
    name: str = Field(...)
    torrent_link: str = Field(...)
    homepage: str | None = Field(None)


class FileSet(BaseModel):
    media_path: str = Field(...)
    sc_subtitle: str | None = Field(None)
    tc_subtitle: str | None = Field(None)


class EpisodeFile(BaseModel):
    media_path: str = Field(...)
    group: str | None = Field(None)
    title: str = Field(...)
    season: int = Field(...)
    episode: int = Field(None)
    suffix: str = Field(..., regex=r"\.(mkv|mp4|MKV|MP4)$")


class SubtitleFile(BaseModel):
    media_path: str = Field(...)
    group: str | None = Field(None)
    title: str = Field(...)
    season: int = Field(...)
    episode: int = Field(None)
    language: str = Field(..., regex=r"(zh|zh-tw)")
    suffix: str = Field(..., regex=r"\.(ass|srt|ASS|SRT)$")
