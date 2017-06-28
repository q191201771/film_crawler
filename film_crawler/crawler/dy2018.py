#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from film_crawler.base import logger
from film_crawler.data import FilmDownloadInfo
from .base import FilmDownloadInfoCrawler


class Dy2018Crawler(FilmDownloadInfoCrawler):
    def __init__(self):
        FilmDownloadInfoCrawler.__init__(self)
        logger.info('> 初始化dy2018.com验证信息...')
        driver = webdriver.Firefox()
        driver.get('http://www.dy2018.com')
        time.sleep(5)
        cookie_list = driver.get_cookies()
        self.cookies = {}
        for cookie in cookie_list:
            self.cookies[cookie['name']] = cookie['value']
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0'
        }
        logger.info('< 初始化dy2018.com验证信息完成.')

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
            resp_content = requests.post(url, data=data, timeout=60, cookies=self.cookies, headers=self.headers).content.decode('gbk')

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
