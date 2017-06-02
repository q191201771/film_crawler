# -*- coding: utf-8 -*-

import sys
import time
from crawler.douban import DoubanCrawler
from crawler.dy2018 import Dy2018Crawler
from crawler.dytt8 import Dytt8Crawler

# 进入豆瓣个人主页，url后缀ID就是豆瓣用户ID，例如我的
# https://www.douban.com/people/77292145/
DOUBAN_USER_ID = '77292145'

if __name__ == '__main__':
    douban_crawler = DoubanCrawler()
    print('> 开始抓取豆瓣用户[ID:%s]想看的电影...' % DOUBAN_USER_ID)
    films = douban_crawler.crawl(DOUBAN_USER_ID)
    print('< 抓取结束，共[%d]部想看的电影.' % len(films))

    download_info_crawlers = [
        Dytt8Crawler(),
        Dy2018Crawler()
    ]

    for film in films:
        print('> 开始抓取电影名[%s]的下载页面...' % film.name)
        for c in download_info_crawlers:
            film.download_info_list = c.crawl(film.name)
            if len(film.download_info_list) == 0:
                continue
            for download_info in film.download_info_list:
                print('  %s - %s' % (download_info.title, download_info.url))
        time.sleep(1)
