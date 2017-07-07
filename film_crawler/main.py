#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

from film_crawler.base import logger, Helper, Config
from film_crawler.crawler import DoubanCrawler, FilmDownloadInfoCrawlerFactory
from film_crawler.data import PersistenceFilmQueryInfo, StatFilmQueryInfo


def film_query_info_wrapper():
    logger.info('豆瓣用户[ID:{}][{}]的电影'.format(Config.DOUBAN_USER_ID, Config.DOUBAN_FILM_QUERY_INFO_TYPE_READABLE))
    films = []
    if Config.IS_LOAD_FILM_QUERY_INFO_FROM_FILE:
        logger.info('> 开始读取本地文件...')
        films = PersistenceFilmQueryInfo.load_from_file(Config.DOUBAN_FILM_QUERY_INFO_FILENAME)
        logger.info('< 读取结束，共[{}]部.'.format(len(films)))
    else:
        logger.info('> 开始抓取...')
        douban_crawler = DoubanCrawler()
        films = douban_crawler.crawl(Config.DOUBAN_USER_ID, Config.DOUBAN_FILM_QUERY_INFO_TYPE,
                                     Config.IS_FETCH_FILM_QUERY_DETAIL_INFO)
        if Config.IS_SAVE_FILM_QUERY_INFO_TO_FILE:
            PersistenceFilmQueryInfo.save_to_file(films, Config.DOUBAN_FILM_QUERY_INFO_FILENAME)
        logger.info('< 抓取结束，共[{}]部.'.format(len(films)))

    if Config.IS_STAT_FILM_QUERY_INFO:
        StatFilmQueryInfo.stat_type_list(films, '类型词云图.png')
        StatFilmQueryInfo.stat_cast_list(films, '演员词云图.png')
        StatFilmQueryInfo.stat_director_list(films, '导演词云图.png')
        StatFilmQueryInfo.stat_writer_list(films, '编剧词云图.png')
        StatFilmQueryInfo.stat_country_list(films, '发行国家词云图.png')

    return films


def film_download_info_wrapper(films):
    download_info_crawlers = [
        # FilmDownloadInfoCrawlerFactory('dy2018'),
        FilmDownloadInfoCrawlerFactory('dytt8'),
        FilmDownloadInfoCrawlerFactory('btrenren')
    ]

    for film in films:
        logger.info('> 开始抓取电影名[{}]的下载页面({} {})...'.format(film.name, film.detail_info.douban_rate,
                                                                   film.detail_info.douban_rate_people))
        for c in download_info_crawlers:
            film.download_info_list = c.crawl(film.name)
            for download_info in film.download_info_list:
                logger.info('  {} - {}'.format(download_info.title, download_info.url))
        Helper.sleep_uniform(Config.CRAWL_INTERVAL_MIN_SEC, Config.CRAWL_INTERVAL_MAX_SEC)

if __name__ == '__main__':
    films= film_query_info_wrapper()
    if Config.IS_FETCH_FILM_DOWNLOAD_INFO:
        film_download_info_wrapper(films)
    logger.info('bye...')
