# -*- coding: utf-8 -*-

class FilmQueryInfoCrawler(object):
    def crawl(self, userid):
        raise NotImplementedError

class FilmDownloadInfoCrawler(object):
    def crawl(self, title):
        raise NotImplementedError
