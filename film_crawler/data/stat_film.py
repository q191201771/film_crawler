#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

from collections import defaultdict
from wordcloud import WordCloud


class StatFilmQueryInfo(object):
    @staticmethod
    def stat_type_list(film_query_info_list, filename):
        frequencies = defaultdict(lambda: 0.0)
        for item in film_query_info_list:
            for t in item.detail_info.type_list:
                if t:
                    frequencies[t] += 1

        StatFilmQueryInfo.save_word_cloud(frequencies, filename)

    @staticmethod
    def stat_cast_list(film_query_info_list, filename):
        frequencies = defaultdict(lambda: 0.0)
        for item in film_query_info_list:
            for t in item.detail_info.cast_list:
                if t:
                    frequencies[t] += 1

        StatFilmQueryInfo.save_word_cloud(frequencies, filename)

    @staticmethod
    def save_word_cloud(frequencies, filename):
        wc = WordCloud(font_path='Arial Unicode.ttf', background_color='white', height=400, width=800)
        wc.generate_from_frequencies(frequencies)
        wc.to_image().show()
        wc.to_file(filename)
