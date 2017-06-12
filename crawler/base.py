#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import csv
from data import FilmQueryInfo
from base import logger

class FilmQueryInfoCrawler(object):
    def __init__(self):
        self.film_query_info_array = []

    def crawl(self, userid):
        raise NotImplementedError

    def save_to_file(self, filename='film_query_info.csv'):
        with open(filename, 'w') as file:
            writer = csv.writer(file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            for item in self.film_query_info_array:
                try:
                    writer.writerow([item.origin_name, item.name])
                except UnicodeEncodeError:
                    pass
                    #logger.warn('FilmQueryInfoCrawler::save_to_file failed. {} {}'.format(item.origin_name, item.name))

    def load_from_file(self, filename='film_query_info.csv'):
        with open(filename) as file:
            reader = csv.reader(file, delimiter=' ', quotechar='|')
            for row in reader:
                if len(row) != 2:
                    continue
                self.film_query_info_array.append(FilmQueryInfo(origin_name=row[0], name=row[1]))

        return self.film_query_info_array


class FilmDownloadInfoCrawler(object):
    def __init__(self):
        self.max_item_limit = 8

    def crawl(self, title):
        raise NotImplementedError

    # 抓回来的下载页面太多，直接不要了~
    def check_max_item_limit(self, item_length):
        return item_length <= self.max_item_limit
