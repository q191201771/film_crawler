#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file   numpy_test.py
# @author
#   chef <191201771@qq.com>
#     -created 2017-06-22 16:52:10
#     -initial release xxxx-xx-xx
# @brief
#   xxx

import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['simhei']
    plt.rcParams['axes.unicode_minus'] = False

    data = pd.read_csv('query_info_collect.csv', names=['origin_name', 'name', 'douban_rate', 'douban_rate_people',
                                                        'director', 'writer', 'cast', 'type', 'country', 'release_time',
                                                        'duration'])

    def save_bar(data, title, xlabel, ylabel):
        fig = plt.figure()
        ax = fig.add_subplot(data.plot(kind='bar'))
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.legend()
        plt.grid(True)
        plt.savefig(title+'.png')

    # 去除空数据 -> 取年份 -> 计数统计 -> 取计数前30个 -> 按年份排序
    rt_counts = data['release_time'].dropna().apply(lambda x: x[0:4]).value_counts()[:30].sort_index()
    print(rt_counts)
    save_bar(rt_counts, '发行年份柱状图', '发行时间', '电影数')

    # 去除空数据 -> 转int -> 计数统计 -> 按评分排序
    dr_counts = data['douban_rate'].dropna().apply(lambda x: int(x)).value_counts().sort_index()
    print(dr_counts)
    save_bar(dr_counts, '豆瓣评分柱状图', '豆瓣评分', '电影数')

    exit(0)
