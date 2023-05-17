from pydantic import BaseModel, Field
from dataclasses import dataclass


class BangumiData(BaseModel):
    id: int | None = Field(None, alias="id", title="番剧ID")
    official_title: str = Field(..., alias="official_title", title="番剧中文名")
    year: int | None = Field(None, alias="year", title="番剧年份")
    title_raw: str = Field(..., alias="title_raw", title="番剧原名")
    season: int = Field(..., alias="season", title="番剧季度")
    season_raw: str = Field(..., alias="season_raw", title="番剧季度原名")
    group: str = Field(..., alias="group", title="字幕组")
    dpi: str = Field(..., alias="dpi", title="分辨率")
    source: str | None = Field(..., alias="source", title="来源")
    subtitle: str | None = Field(..., alias="subtitle", title="字幕")
    added: bool = Field(False, alias="added", title="是否已添加")
    eps_collect: bool = Field(False, alias="eps_collect", title="是否已收集")
    offset: int = Field(0, alias="offset", title="番剧偏移量")
    filter: list[str] = Field(..., alias="filter", title="番剧过滤器")


class ProgramData(BaseModel):
    rss_link: str = Field(..., alias="rss_link", title="RSS链接")
    data_version: float = Field(..., alias="data_version", title="数据版本")
    bangumi_info: list[BangumiData] = Field([], alias="bangumi_info", title="番剧信息")


@dataclass
class MatchRule:
    keyword: str
    filter: list
    rss_link: str


@dataclass
class GroupFilter:
    name: str
    filter: list


@dataclass
class Episode:
    title_en: str | None
    title_zh: str | None
    title_jp: str | None
    season: int
    season_raw: str
    episode: int
    sub: str
    group: str
    resolution: str
    source: str


@dataclass
class SeasonInfo(dict):
    official_title: str
    title_raw: str
    season: int
    season_raw: str
    group: str
    filter: list | None
    offset: int | None
    dpi: str
    source: str
    subtitle: str
    added: bool
    eps_collect: bool



