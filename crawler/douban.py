#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import requests
from bs4 import BeautifulSoup
from . import FilmQueryInfoCrawler
from data import FilmQueryInfo, FilmQueryDetailInfo
from base import Helper


class DoubanCrawler(FilmQueryInfoCrawler):
    def crawl(self, userid, is_fetch_detail_info=False):
        """return Film list"""
        url = 'https://movie.douban.com/people/{userid}/wish'.format(userid = userid)
        params = {
            'start':  '0',
            'sort':   'time',
            'rating': 'all',
            'filter': 'all',
            'mode':   'grid'
        }

        try:
            while True:
                resp = requests.get(url=url, params=params, timeout=30)
                soup = BeautifulSoup(resp.content, 'html.parser')

                for item in soup.select('.article .grid-view .item .info .title a'):
                    origin_name = item.em.string
                    item_url = item['href']
                    film = FilmQueryInfo(origin_name=origin_name, name=origin_name.split('/')[0].strip(), douban_url=item_url)
                    self.film_query_info_array.append(film)

                    if is_fetch_detail_info:
                        film.detail_info = self.crawlDetailInfo(film.douban_url)
                        Helper.sleep_uniform(0.5, 1)

                next_page = soup.select('.article .paginator .next a')
                if len(next_page) != 1:
                    break
                params = None
                url = next_page[0]['href']

                Helper.sleep_uniform(0.5, 1)
        except Exception as e:
            pass

        return self.film_query_info_array

    def crawlDetailInfo(self, url):
        resp = requests.get(url=url, timeout=30)
        soup = BeautifulSoup(resp.content, 'html.parser')

        info = FilmQueryDetailInfo()
        douban_rate = soup.select('.ll.rating_num')
        if len(douban_rate) == 1:
            info.douban_rate = douban_rate[0].string
        douban_rate_people = soup.select('.rating_people span')
        if len(douban_rate_people) == 1:
            info.douban_rate_people = int(douban_rate_people[0].string)

        return info
