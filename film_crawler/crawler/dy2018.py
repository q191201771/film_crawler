#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import requests
from bs4 import BeautifulSoup

from film_crawler.base import logger
from film_crawler.data import FilmDownloadInfo
from .base import FilmDownloadInfoCrawler


class Dy2018Crawler(FilmDownloadInfoCrawler):
    def crawl(self, name):
        """@return FilmDownloadInfo list"""
        film_download_info_list = []
        url = 'http://www.dy2018.com/e/search/index.php'
        data = {
            'show':     'title,smalltext',
            'tempid':   '1',
            'keyboard': name.encode('gbk'),
            'Submit':   u'立即搜索'.encode('gbk')
        }

        try:
            resp_content = requests.post(url, data=data, timeout=60).content.decode('gbk')

            soup = BeautifulSoup(resp_content, 'html.parser')
            items = soup.select('.co_content8 a.ulink')
            for item in items:
                title = item.string
                info_url = 'http://www.dy2018.com'+item['href']
                film_download_info_list.append(FilmDownloadInfo(title=title, url=info_url))
        except UnicodeDecodeError:
            pass
        except Exception as e:
            logger.warn(e)

        return self.filter(name, film_download_info_list)
