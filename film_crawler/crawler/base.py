#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx


class FilmQueryInfoCrawler(object):
    def __init__(self):
        self.film_query_info_list = []

    def crawl(self, userid, query_info_type, is_fetch_detail_info):
        raise NotImplementedError


class FilmDownloadInfoCrawler(object):
    def __init__(self):
        self.max_item_for_filter = 16
        self.keyword_for_filter = ['单机游戏']

    def crawl(self, name):
        raise NotImplementedError

    def filter(self, title, film_download_info_list):
        return self.keyword_filter(title, self.max_item_filter(film_download_info_list))

    # 抓回来的下载页面太多
    def max_item_filter(self, film_download_info_list):
        return film_download_info_list if len(film_download_info_list) < self.max_item_for_filter else []

    # 关键词过滤
    def keyword_filter(self, title, film_download_info_list):
        result = []
        # 待抓取的标题中包含的过滤关键字
        keyword = [k for k in self.keyword_for_filter if k not in title]
        if not keyword:
            return film_download_info_list
        for film in film_download_info_list:
            # 当前的下载标题中包含过滤关键字
            if [k for k in keyword if k in film.title]:
                continue
            result.append(film)
        return result
