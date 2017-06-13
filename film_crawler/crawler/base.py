#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx


class FilmQueryInfoCrawler(object):
    def __init__(self):
        self.film_query_info_list = []

    def crawl(self, userid):
        raise NotImplementedError


class FilmDownloadInfoCrawler(object):
    def __init__(self):
        self.max_item_limit = 8

    def crawl(self, title):
        raise NotImplementedError

    # 抓回来的下载页面太多，直接不要了~
    def check_max_item_limit(self, item_length):
        return item_length <= self.max_item_limit
