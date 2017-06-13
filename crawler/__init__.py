#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

from .base import FilmQueryInfoCrawler, FilmDownloadInfoCrawler
from .factory import film_download_info_crawler_factory
from .douban import DoubanCrawler
from .dy2018 import Dy2018Crawler
from .dytt8 import Dytt8Crawler

__all__ = ['FilmQueryInfoCrawler', 'FilmDownloadInfoCrawler', 'film_download_info_crawler_factory', 'DoubanCrawler',
           'Dy2018Crawler', 'Dytt8Crawler']