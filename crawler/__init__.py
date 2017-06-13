#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

from .base import FilmQueryInfoCrawler, FilmDownloadInfoCrawler
from .douban import DoubanCrawler
from .dy2018 import Dy2018Crawler
from .dytt8 import Dytt8Crawler

__all__ = ['FilmQueryInfoCrawler', 'FilmDownloadInfoCrawler', 'DoubanCrawler', 'Dy2018Crawler', 'Dytt8Crawler']