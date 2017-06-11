# -*- coding: utf-8 -*-

class FilmQueryInfoCrawler(object):
    def crawl(self, userid):
        raise NotImplementedError

class FilmDownloadInfoCrawler(object):
    max_item_limit = 8

    def crawl(self, title):
        raise NotImplementedError

    # 抓回来的下载页面太多，直接不要了~
    def check_max_item_limit(self, item_length):
        return item_length <= self.max_item_limit
