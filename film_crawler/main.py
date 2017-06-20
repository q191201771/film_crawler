#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

from film_crawler.base import logger, Helper, Config
from film_crawler.crawler import DoubanCrawler, film_download_info_crawler_factory
from film_crawler.data import PersistenceFilmQueryInfo


def fetch_film_query_info():
    films = []
    if Config.IS_LOAD_FILM_QUERY_INFO_FROM_FILE:
        logger.info('> 开始读取本地文件中缓存想看的电影...')
        films = PersistenceFilmQueryInfo.load_from_file()
        logger.info('< 读取结束，共[{}]部想看的电影.'.format(len(films)))
    else:
        logger.info('> 开始抓取豆瓣用户[ID:{}]想看的电影...'.format(Config.DOUBAN_USER_ID))
        douban_crawler = DoubanCrawler()
        films = douban_crawler.crawl(Config.DOUBAN_USER_ID, Config.IS_FETCH_FILM_QUERY_DETAIL_INFO)
        if Config.IS_SAVE_FILM_QUERY_INFO_TO_FILE:
            PersistenceFilmQueryInfo.save_to_file(films)
        logger.info('< 抓取结束，共[{}]部想看的电影.'.format(len(films)))

    return films

if __name__ == '__main__':
    films= fetch_film_query_info()

    download_info_crawlers = [
        film_download_info_crawler_factory('dy2018'),
        film_download_info_crawler_factory('dytt8')
    ]

    for film in films:
        if film.detail_info is None:
            logger.info('> 开始抓取电影名[{}]的下载页面...'.format(film.name))
        else:
            logger.info('> 开始抓取电影名[{}]的下载页面({} {})...'.format(film.name, film.detail_info.douban_rate,
                                                                        film.detail_info.douban_rate_people))
        for c in download_info_crawlers:
            film.download_info_list = c.crawl(film.name)
            for download_info in film.download_info_list:
                logger.info('  {} - {}'.format(download_info.title, download_info.url))
        Helper.sleep_uniform(Config.CRAWL_INTERVAL_MIN_SEC, Config.CRAWL_INTERVAL_MAX_SEC)

    logger.info('bye...')