#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  配置项


class Config:
    class ConstError(TypeError):
        pass

    def __setattr__(self, key, value):
        raise self.ConstError('Can not change const.{}'.format(key))

    # 进入豆瓣个人主页，url后缀ID就是豆瓣用户ID，例如我的 https://www.douban.com/people/77292145/
    DOUBAN_USER_ID = '77292145'
    # 不从豆瓣抓想看电影，直接从本地文件加载
    IS_LOAD_FILM_QUERY_INFO_FROM_FILE = False
    # 从豆瓣抓取完想看电影后，是否写入本地文件中
    IS_SAVE_FILM_QUERY_INFO_TO_FILE = True
    # 是否从豆瓣抓取评分等详细信息
    IS_FETCH_FILM_QUERY_DETAIL_INFO = True
    # 抓取间隔时间最小值
    CRAWL_INTERVAL_MIN_SEC = 0.3
    # 抓取间隔时间最大值
    CRAWL_INTERVAL_MAX_SEC = 0.7
    # UA
    CRAWLER_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    # 最简单的http request header
    CRAWLER_BASIC_HEADERS = {
        'User-Agent': CRAWLER_USER_AGENT
    }
