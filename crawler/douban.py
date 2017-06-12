#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import time
import requests
from bs4 import BeautifulSoup
from crawler.base import FilmQueryInfoCrawler
from data.film import FilmQueryInfo

class DoubanCrawler(FilmQueryInfoCrawler):
    def crawl(self, userid):
        """return Film list"""
        # return self._mock_crawl()
        films = []
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
                    film = FilmQueryInfo(origin_name=origin_name, name=origin_name.split('/')[0].strip())
                    films.append(film)

                next_url_tags = soup.select('.article .paginator .next a')
                if len(next_url_tags) != 1:
                    break
                params = None
                url = next_url_tags[0]['href']

                time.sleep(1)
        except Exception as e:
            return films

        return films

    def _mock_crawl(self):
        return []
