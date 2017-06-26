#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file   numpy_test.py
# @author
#   chef <191201771@qq.com>
#     -created 2017-06-22 16:52:10
#     -initial release xxxx-xx-xx
# @brief
#   学习下pyplot画图

import pandas as pd
import matplotlib.pyplot as plt


def save_basic_image(data, xlabel, ylabel, kind):
    kind_readable_mapping = {
        'line': '折线图',
        'bar': '柱状图'
    }
    title = '{}-{}{}'.format(xlabel, ylabel, kind_readable_mapping[kind])
    filename = title+'.png'

    fig = plt.figure(figsize=(10.24, 7.68))
    # ax = fig.add_subplot(data.plot(label=xlabel, kind=kind))
    ax = fig.add_subplot(1, 1, 1)
    data.plot(ax=ax, label=xlabel, kind=kind)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.legend() # 图例
    plt.grid(True) # 网格
    plt.savefig(filename)


def cleaning_country(x):
    x = x.split('/')[0]
    mapping = {
        '中国大陆': '中国',
        '香港': '中国香港'
    }
    return x if x not in mapping else mapping[x]

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['simhei']
    plt.rcParams['axes.unicode_minus'] = False

    data = pd.read_csv('query_info_collect.csv', names=['origin_name', 'name', 'douban_rate', 'douban_rate_people',
                                                        'director', 'writer', 'cast', 'type', 'country', 'release_time',
                                                        'duration'])

    # *** 清洗数据
    # 1. 去掉NA数据
    data = data.dropna()
    # 2. 国家字段
    #   a) 取'/'分隔符的一个
    #   b) 含义相同名字不同的合并
    data['country'] = data['country'].apply(cleaning_country)

    # ***
    dr_country = data[['douban_rate', 'country']]
    dr_country = dr_country.groupby('country').mean().sort_values(by='douban_rate')
    print(dr_country)
    save_basic_image(dr_country, '发行国家', '豆瓣评分', 'bar')

    # *** 去除空数据 -> 取年份 -> 计数统计 -> 取计数前30个 -> 按年份排序
    rt_counts = data['release_time'].dropna().apply(lambda x: x[0:4]).value_counts()[:].sort_index()
    print(rt_counts)
    save_basic_image(rt_counts, '发行年份', '电影数', 'bar')

    # *** 去除空数据 -> 转int -> 计数统计 -> 按评分排序
    dr_counts = data['douban_rate'].dropna().apply(lambda x: int(x)).value_counts().sort_index()
    print(dr_counts)
    save_basic_image(dr_counts, '豆瓣评分', '电影数', 'line')

    exit(0)
