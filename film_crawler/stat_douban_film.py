#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file   numpy_test.py
# @author
#   chef <191201771@qq.com>
#     -created 2017-06-22 16:52:10
#     -initial release xxxx-xx-xx
# @brief
#   学习下pyplot画图

import random

import pandas as pd
import matplotlib.pyplot as plt


class Colors(object):
    def __init__(self):
        self.colors = ['#e51c23', '#e91e63', '#9c27b0', '#673ab7', '#3f51b5', '#5677fc',
                       '#03a9f4', '#00bcd4', '#009688', '#259b24', '#8bc34a', '#cddc39',
                       '#ffeb3b', '#ffc107', '#ff9800', '#ff5722', '#795548', '#9e9e9e',
                       '#607d8b']
        # self.colors = ['#e00032', '#c51162', '#aa00ff', '#6200ea', '#304ffe', '#4d69ff', '#0091ea', '#00b8d4', '#00bfa5']
        self.i = 0

    def next(self):
        c = self.colors[self.i % len(self.colors)]
        self.i += 1
        return c


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
                                                        'duration', 'mark_time'])

    # *** 清洗数据
    # 1. 去掉NA数据
    data = data.dropna()
    # 2. 国家字段
    #   a) 取'/'分隔符的一个
    #   b) 含义相同名字不同的合并
    data['country'] = data['country'].apply(cleaning_country)

    # ***
    fig = plt.figure(figsize=(20.48, 15.36))
    ax = fig.add_subplot(1, 1, 1)
    colors = Colors()
    for country, _ in data.groupby('country'):
        data[data.country == country].plot(ax=ax, x='douban_rate', y='douban_rate_people', marker='x',
                                           # c=(random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)),
                                           c=colors.next(),
                                           label=country, kind='scatter')
    ax.set_title('豆瓣评分及评分人数散点图')
    ax.set_xlabel('豆瓣评分')
    ax.set_ylabel('评分人数')
    plt.legend() # 图例
    plt.grid(True) # 网格
    plt.savefig('豆瓣评分及评分人数散点图.png')

    # ***
    mt_country = data[['mark_time', 'country']].copy()
    mt_country['mark_time'] = mt_country['mark_time'].apply(lambda x: x[0:4])
    fig = plt.figure(figsize=(10.24, 7.68))
    ax = fig.add_subplot(1, 1, 1)
    all_mt_count = mt_country['mark_time'].dropna().value_counts()
    for country, group in mt_country.groupby('country'):
        # print(country)
        mt_counts = group['mark_time'].value_counts().sort_index()
        mt_counts = mt_counts / all_mt_count
        mt_counts.plot(ax=ax, label=country, kind='line')
    ax.set_title('每年观看电影各发行国家占比')
    ax.set_xlabel('观看时间')
    ax.set_ylabel('比例')
    plt.legend()
    plt.savefig('每年观看电影各发行国家占比.png')

    # ***
    dr_country = data[['douban_rate', 'country']]
    dr_country = dr_country.groupby('country').mean().sort_values(by='douban_rate')
    # print(dr_country)
    save_basic_image(dr_country, '发行国家', '豆瓣评分', 'bar')

    # *** 去除空数据 -> 取年份 -> 计数统计 -> [取计数前x个] -> 按年份排序
    rt_counts = data['release_time'].dropna().apply(lambda x: x[0:4]).value_counts()[:].sort_index()
    # print(rt_counts)
    save_basic_image(rt_counts, '发行年份', '电影数', 'bar')

    # *** 去除空数据 -> 转int -> 计数统计 -> 按评分排序
    dr_counts = data['douban_rate'].dropna().apply(lambda x: int(x)).value_counts().sort_index()
    # print(dr_counts)
    save_basic_image(dr_counts, '豆瓣评分', '电影数', 'line')

    # *** 去除空数据 -> 转int -> 计数统计 -> 按评分排序
    c_counts = data['country'].dropna().value_counts()
    # print(c_counts)
    save_basic_image(c_counts, '发行国家', '电影数', 'bar')

    # *** 去除空数据 -> 取年月 -> 计数统计 -> [取计数前x个] -> 按年月排序
    mt_counts = data['mark_time'].dropna().apply(lambda x: x[0:7]).value_counts()[:].sort_index()
    # print(mt_counts)
    save_basic_image(mt_counts, '观看时间', '电影数', 'bar')

