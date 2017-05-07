# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from crawler.base import FilmDownloadInfoCrawler
from data.film  import FilmDownloadInfo

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
        except Exception, e:
            #print 'oops~ [%s] [%s:%s]' % (name, self.__class__, e)
            return film_download_info_list
        soup = BeautifulSoup(resp_content, 'html.parser')
        for item in soup.select('.co_content8 table a'):
            item.font.unwrap()
            title = ''.join(item.contents)
            info_url = 'http://s.dydytt.net'+item['href']
            film_download_info_list.append(FilmDownloadInfo(title=title, url=info_url))
        return film_download_info_list
