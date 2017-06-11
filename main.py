# -*- coding: utf-8 -*-

import time
from base.log import logger
from crawler.douban import DoubanCrawler
from crawler.dy2018 import Dy2018Crawler
from crawler.dytt8 import Dytt8Crawler

# 进入豆瓣个人主页，url后缀ID就是豆瓣用户ID，例如我的
# https://www.douban.com/people/77292145/
DOUBAN_USER_ID = '77292145'

if __name__ == '__main__':
    douban_crawler = DoubanCrawler()
    logger.info('> 开始抓取豆瓣用户[ID:{}]想看的电影...'.format(DOUBAN_USER_ID))
    films = douban_crawler.crawl(DOUBAN_USER_ID)
    logger.info('< 抓取结束，共[{}]部想看的电影.'.format(len(films)))

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
