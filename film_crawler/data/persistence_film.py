#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import csv
from . import FilmQueryInfo


class PersistenceFilmQueryInfo(object):
    @staticmethod
    def save_to_file(film_query_info_list, filename='film_query_info.csv'):
        with open(filename, 'w') as file:
            writer = csv.writer(file)

            for item in film_query_info_list:
                try:
                    if item.detail_info is None:
                        writer.writerow([item.origin_name, item.name])
                    else:
                        writer.writerow([item.origin_name,
                                         item.name,
                                         item.detail_info.douban_rate,
                                         item.detail_info.douban_rate_people,
                                         item.detail_info.director,
                                         item.detail_info.writer,
                                         ''.join(item.detail_info.type_list),
                                         item.detail_info.country,
                                         item.detail_info.release_time,
                                         item.detail_info.duration])
                except UnicodeEncodeError:
                    pass

    @staticmethod
    def load_from_file(filename='film_query_info.csv'):
        film_query_info_list = []
        with open(filename) as file:
            reader = csv.reader(file, delimiter=' ', quotechar='|')
            for row in reader:
                if len(row) >= 2:
                    film = FilmQueryInfo(origin_name=row[0], name=row[1])
                    if len(row) > 2:
                        film.detail_info.douban_rate = row[2]
                        film.detail_info.douban_rate_people = row[3]
                        # TODO
                    film_query_info_list.append(film)

        return film_query_info_list
