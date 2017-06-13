#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx


class FilmQueryDetailInfo(object):
    def __init__(self):
        self.douban_rate = None
        self.douban_rate_people = None
        self.director = None
        self.writer = None
        self.cast_list = []
        self.type_list = []
        self.country = None # TODO can be list
        self.lang = None # can be list
        self.release_time = None # can be list
        self.duration = None
        self.alias = None # can be list
        self.imdb = None


class FilmDownloadInfo(object):
    def __init__(self, title, url):
        self.title = title
        self.url = url


class FilmQueryInfo(object):
    def __init__(self, origin_name, name, douban_url, download_info_list=None, douban_rate=None, douban_rate_count=None):
        self.origin_name = origin_name
        self.name = name
        self.douban_url = douban_url

        self.detail_info = None

        self.download_info_list = download_info_list if download_info_list is not None else []

