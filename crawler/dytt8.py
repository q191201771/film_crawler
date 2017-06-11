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

            soup = BeautifulSoup(resp_content, 'html.parser')
            items = soup.select('.co_content8 table a')
            if self.check_max_item_limit(len(items)) is not True:
                return film_download_info_list
            for item in items:
                item.font.unwrap()
                title = ''.join(item.contents)
                info_url = 'http://s.dydytt.net'+item['href']
                film_download_info_list.append(FilmDownloadInfo(title=title, url=info_url))
        except Exception as e:
            return film_download_info_list

        return film_download_info_list
