#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

from collections import defaultdict
from wordcloud import WordCloud


class StatFilmQueryInfo(object):
    @staticmethod
    def stat_type_list(film_query_info_list, filename):
        stat_at_detail_info(film_query_info_list, filename, 'type_list')

    @staticmethod
    def stat_cast_list(film_query_info_list, filename):
        stat_at_detail_info(film_query_info_list, filename, 'cast_list')

    @staticmethod
    def stat_director_list(film_query_info_list, filename):
        stat_at_detail_info(film_query_info_list, filename, 'director_list')

    @staticmethod
    def stat_writer_list(film_query_info_list, filename):
        stat_at_detail_info(film_query_info_list, filename, 'writer_list')

    @staticmethod
    def stat_country_list(film_query_info_list, filename):
        stat_at_detail_info(film_query_info_list, filename, 'country_list')


def stat_at_detail_info(film_query_info_list, filename, attrname):
    frequencies = defaultdict(lambda: 0.0)
    for film in film_query_info_list:
        for item in film.detail_info.__dict__[attrname]:
            if item:
                frequencies[item] += 1

    save_word_cloud(frequencies, filename)


def save_word_cloud(frequencies, filename):
    wc = WordCloud(font_path='Arial Unicode.ttf', background_color='white', height=400, width=800)
    wc.generate_from_frequencies(frequencies)
    # wc.to_image().show()
    wc.to_file(filename)
