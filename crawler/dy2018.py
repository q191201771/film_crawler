# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from crawler.base import FilmDownloadInfoCrawler
from data.film  import FilmDownloadInfo

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
        except Exception, e:
            #print 'oops~ [%s] [%s:%s]' % (name, self.__class__, e)
            return film_download_info_list
        soup = BeautifulSoup(resp_content, 'html.parser')
        for item in soup.select('.co_content8 a.ulink'):
            title = item.string
            info_url = 'http://www.dy2018.com'+item['href']
            film_download_info_list.append(FilmDownloadInfo(title=title, url=info_url))
        return film_download_info_list
