#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

from base import logger, Helper
from crawler import DoubanCrawler, Dy2018Crawler, Dytt8Crawler
from data import PersistenceFilmQueryInfo

##### 一些配置项
# 进入豆瓣个人主页，url后缀ID就是豆瓣用户ID，例如我的 https://www.douban.com/people/77292145/
DOUBAN_USER_ID = '77292145'
# 不从豆瓣抓想看电影，直接从本地文件加载
IS_LOAD_FILM_QUERY_INFO_FROM_FILE = False
# 从豆瓣抓取完想看电影后，是否写入本地文件中
IS_SAVE_FILM_QUERY_INFO_TO_FILE = True
# 是否从豆瓣抓取评分等详细信息
IS_FETCH_FILM_QUERY_DETAIL_INFO = True


def fetch_film_query_info():
    films = []
    if IS_LOAD_FILM_QUERY_INFO_FROM_FILE:
        logger.info('> 开始读取本地文件中缓存想看的电影...')
        films = PersistenceFilmQueryInfo.load_from_file()
        logger.info('< 读取结束，共[{}]部想看的电影.'.format(len(films)))
    else:
        logger.info('> 开始抓取豆瓣用户[ID:{}]想看的电影...'.format(DOUBAN_USER_ID))
        douban_crawler = DoubanCrawler()
        films = douban_crawler.crawl(DOUBAN_USER_ID, IS_FETCH_FILM_QUERY_DETAIL_INFO)
        if IS_SAVE_FILM_QUERY_INFO_TO_FILE:
            PersistenceFilmQueryInfo.save_to_file(films)
        logger.info('< 抓取结束，共[{}]部想看的电影.'.format(len(films)))

    return films

if __name__ == '__main__':
    films= fetch_film_query_info()

    download_info_crawlers = [
        Dytt8Crawler(),
        Dy2018Crawler()
    ]

    for film in films:
        if film.detail_info is None:
            logger.info('> 开始抓取电影名[{}]的下载页面...'.format(film.name))
        else:
            logger.info('> 开始抓取电影名[{}]的下载页面({} {})...'.format(film.name, film.detail_info.douban_rate,
                                                                        film.detail_info.douban_rate_people))
        for c in download_info_crawlers:
            film.download_info_list = c.crawl(film.name)
            if len(film.download_info_list) == 0:
                continue
            for download_info in film.download_info_list:
                logger.info('  {} - {}'.format(download_info.title, download_info.url))
        Helper.sleep_uniform(0.5, 1)

    logger.info('bye...')