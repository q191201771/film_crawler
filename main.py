#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import time
from base import logger
from crawler import DoubanCrawler, Dy2018Crawler, Dytt8Crawler

##### 一些配置项
# 进入豆瓣个人主页，url后缀ID就是豆瓣用户ID，例如我的 https://www.douban.com/people/77292145/
DOUBAN_USER_ID = '77292145'
# 不从豆瓣抓想看电影，直接从本地文件加载
LOAD_FILM_QUERY_INFO_FROM_FILE = False
# 从豆瓣抓取完想看电影后，是否写入本地文件中
SAVE_FILM_QUERY_INFO_TO_FILE = True

def fetch_film_query_info():
    douban_crawler = DoubanCrawler()
    films = []
    if LOAD_FILM_QUERY_INFO_FROM_FILE:
        logger.info('> 开始读取本地文件中缓存想看的电影...')
        films = douban_crawler.load_from_file()
        logger.info('< 读取结束，共[{}]部想看的电影.'.format(len(films)))
    else:
        logger.info('> 开始抓取豆瓣用户[ID:{}]想看的电影...'.format(DOUBAN_USER_ID))
        films = douban_crawler.crawl(DOUBAN_USER_ID)
        if SAVE_FILM_QUERY_INFO_TO_FILE:
            douban_crawler.save_to_file()
        logger.info('< 抓取结束，共[{}]部想看的电影.'.format(len(films)))

    return films

if __name__ == '__main__':
    films= fetch_film_query_info()

    download_info_crawlers = [
        Dytt8Crawler(),
        Dy2018Crawler()
    ]

    for film in films:
        logger.info('> 开始抓取电影名[{}]的下载页面...'.format(film.name))
        for c in download_info_crawlers:
            film.download_info_list = c.crawl(film.name)
            if len(film.download_info_list) == 0:
                continue
            for download_info in film.download_info_list:
                logger.info('  {} - {}'.format(download_info.title, download_info.url))
        time.sleep(1)

    logger.info('bye...')