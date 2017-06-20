#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import requests
from bs4 import BeautifulSoup

from film_crawler.base import Helper, logger, Config
from film_crawler.data import FilmQueryInfo, FilmQueryDetailInfo
from . import FilmQueryInfoCrawler


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
                    self.film_query_info_list.append(film)

                    if is_fetch_detail_info:
                        film.detail_info = self.crawl_detail_info(film.douban_url)
                        Helper.sleep_uniform(Config.CRAWL_INTERVAL_MIN_SEC, Config.CRAWL_INTERVAL_MAX_SEC)

                next_page = soup.select('.article .paginator .next a')
                if len(next_page) != 1:
                    break
                params = None
                url = next_page[0]['href']

                Helper.sleep_uniform(Config.CRAWL_INTERVAL_MIN_SEC, Config.CRAWL_INTERVAL_MAX_SEC)
        except Exception as e:
            logger.warn(e)

        return self.film_query_info_list

    def crawl_detail_info(self, url):
        resp = requests.get(url=url, timeout=30)
        soup = BeautifulSoup(resp.content, 'html.parser')

        info = FilmQueryDetailInfo()

        douban_rate = soup.select('.ll.rating_num')
        if len(douban_rate) == 1:
            info.douban_rate = douban_rate[0].string
        douban_rate_people = soup.select('.rating_people span')
        if len(douban_rate_people) == 1:
            info.douban_rate_people = int(douban_rate_people[0].string)

        def single_op(value):
            return value.strip()

        def multi_op(value):
            return [item.strip() for item in value.split('/')]

        try:
            info_line_list = soup.select('#info')[0].text.splitlines()
            for info_line in info_line_list:
                kv = info_line.split(':')
                if len(kv) != 2:
                    continue
                k = kv[0].strip()
                v = kv[1].strip()
                # TODO 这里能不能mapping得漂亮点，还是对类对象这块基础知识掌握的不扎实
                if k == '导演': info.director = single_op(v)
                if k == '编剧': info.writer = single_op(v)
                if k == '主演': info.cast_list = multi_op(v)
                if k == '类型': info.type_list = multi_op(v)
                if k == '制片国家/地区': info.country = single_op(v)
                if k == '语言': info.lang = single_op(v)
                if k == '上映日期': info.release_time = single_op(v)
                if k == '片长': info.duration = single_op(v)
                if k == '又名': info.alias = single_op(v)
                if k == 'IMDb链接': info.imdb = single_op(v)

        except IndexError:
            pass
        except Exception as e:
            logger.warn(e)

        return info
