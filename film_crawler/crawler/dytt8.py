#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import requests
from bs4 import BeautifulSoup

from film_crawler.base import logger
from film_crawler.data import FilmDownloadInfo
from .base import FilmDownloadInfoCrawler


class Dytt8Crawler(FilmDownloadInfoCrawler):
    def crawl(self, name):
        """return FilmDownloadInfo list"""
        film_download_info_list = []
        url = 'http://s.dydytt.net/plus/search.php'
        params = {
            'kwtype': 0,
            'keyword': name.encode('gbk')
        }

        try:
            resp_content = requests.get(url, params=params, timeout=30).content.decode('gbk')

            soup = BeautifulSoup(resp_content, 'html.parser')
            items = soup.select('.co_content8 table a')
            for item in items:
                if item.font is not None:
                    item.font.unwrap()
                title = ''.join(item.contents)
                info_url = 'http://s.dydytt.net'+item['href']
                film_download_info_list.append(FilmDownloadInfo(title=title, url=info_url))
        except UnicodeDecodeError:
            pass
        except Exception as e:
            logger.warn(e)

        return self.filter(name, film_download_info_list)
