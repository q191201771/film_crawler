#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx


class FilmQueryInfo:
    def __init__(self, origin_name, name, download_info_list=None, douban_rate=None, douban_rate_count=None):
        self.origin_name = origin_name
        self.name = name
        self.download_info_list = download_info_list if download_info_list is not None else []
        self.douban_rate = douban_rate
        self.douban_rate_count = douban_rate_count


class FilmDownloadInfo:
    def __init__(self, title, url):
        self.title = title
        self.url = url
