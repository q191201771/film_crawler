#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import requests
from bs4 import BeautifulSoup

from film_crawler.base import logger, Config
from film_crawler.data import FilmDownloadInfo
from .base import FilmDownloadInfoCrawler


class BTRenRenCrawler(FilmDownloadInfoCrawler):
    def __init__(self):
        FilmDownloadInfoCrawler.__init__(self)
        self.domain = 'http://www.btrenren.com'

    def crawl(self, name):
        """return FilmDownloadInfo list"""
        film_download_info_list = []
        url = '{}/index.php/Search/index.html'.format(self.domain)
        params = {
            'search': name.encode('utf-8')
        }

        try:
            resp_content = requests.get(url, params=params, timeout=30, headers=Config.CRAWLER_BASIC_HEADERS).content

            soup = BeautifulSoup(resp_content, 'html.parser')
            items = soup.select('body > div.mb.cl > div.ml > div.item > div.title > p.tt.cl > a')
            for item in items:
                title = item['title']
                info_url = '{}{}'.format(self.domain, item['href'])
                film_download_info_list.append(FilmDownloadInfo(title=title, url=info_url))
        except UnicodeDecodeError:
            pass
        except Exception as e:
            logger.warn(e)

        return self.filter(name, film_download_info_list)
