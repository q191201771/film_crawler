#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

from .dy2018 import Dy2018Crawler
from .dytt8 import Dytt8Crawler


def film_download_info_crawler_factory(source):
    mapping = {
        'dy2018': Dy2018Crawler(),
        'dytt8': Dytt8Crawler()
    }
    return mapping[source]