#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx


class FilmQueryDetailInfo(object):
    def __init__(self):
        self.douban_rate = None
        self.douban_rate_people = None
        self.director_list = []
        self.writer_list = []
        self.cast_list = []
        self.type_list = []
        self.country_list = []
        self.lang = None # not persistence
        self.release_time_list = []
        self.duration_list = []
        self.alias = None # not persistence
        self.imdb = None # not persistence


class FilmDownloadInfo(object):
    def __init__(self, title, url):
        self.title = title
        self.url = url


class FilmQueryInfo(object):
    def __init__(self, origin_name, name, douban_url=None, download_info_list=None, douban_rate=None, douban_rate_count=None):
        self.origin_name = origin_name
        self.name = name
        self.douban_url = douban_url

        self.detail_info = FilmQueryDetailInfo()

        self.download_info_list = download_info_list if download_info_list is not None else []

