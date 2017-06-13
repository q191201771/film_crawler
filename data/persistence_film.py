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
            writer = csv.writer(file, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            for item in film_query_info_array:
                try:
                    writer.writerow([item.origin_name, item.name])
                except UnicodeEncodeError:
                    pass

    @staticmethod
    def load_from_file(filename='film_query_info.csv'):
        film_query_info_array = []
        with open(filename) as file:
            reader = csv.reader(file, delimiter=' ', quotechar='|')
            for row in reader:
                if len(row) != 2:
                    continue
                film_query_info_array.append(FilmQueryInfo(origin_name=row[0], name=row[1]))
        return film_query_info_array
