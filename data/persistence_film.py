#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import csv
from . import FilmQueryInfo


class PersistenceFilmQueryInfo(object):
    @staticmethod
    def save_to_file(film_query_info_array, filename='film_query_info.csv'):
        with open(filename, 'w') as file:
            writer = csv.writer(file)

            for item in film_query_info_array:
                try:
                    if item.detail_info is None:
                        writer.writerow([item.origin_name, item.name])
                    else:
                        writer.writerow([item.origin_name, item.name, item.detail_info.douban_rate, item.detail_info.douban_rate_people])
                except UnicodeEncodeError:
                    pass

    @staticmethod
    def load_from_file(filename='film_query_info.csv'):
        film_query_info_array = []
        with open(filename) as file:
            reader = csv.reader(file, delimiter=' ', quotechar='|')
            for row in reader:
                if len(row) >= 2:
                    film = FilmQueryInfo(origin_name=row[0], name=row[1])
                    if len(row) > 2:
                        film.detail_info.douban_rate = row[2]
                        film.detail_info.douban_rate_people = row[3]
                    film_query_info_array.append(film)

        return film_query_info_array
