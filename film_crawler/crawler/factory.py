#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

from .dy2018 import Dy2018Crawler
from .dytt8 import Dytt8Crawler
from .base import FilmDownloadInfoCrawler


class FilmDownloadInfoCrawlerFactory(object):
    crawlers = {'dy2018': Dy2018Crawler,
                'dytt8': Dytt8Crawler}

    def __new__(cls, name):
        if name in cls.crawlers:
            return cls.crawlers[name]()
        else:
            return FilmDownloadInfoCrawler()
