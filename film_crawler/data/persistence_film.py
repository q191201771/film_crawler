#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import csv
from . import FilmQueryInfo
from film_crawler.base import logger


class PersistenceFilmQueryInfo(object):
    @staticmethod
    def save_to_file(film_query_info_list, filename='film_query_info.csv'):
        with open(filename, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, lineterminator='\n')

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
                                         '/'.join(item.detail_info.type_list),
                                         item.detail_info.country,
                                         item.detail_info.release_time,
                                         item.detail_info.duration])
                except UnicodeEncodeError:
                    pass
                except Exception as e:
                    logger.warn(e)

    @staticmethod
    def load_from_file(filename='film_query_info.csv'):
        film_query_info_list = []
        with open(filename, encoding='utf-8') as file:
            reader = csv.reader(file, lineterminator='\n')
            for row in reader:
                film = FilmQueryInfo(origin_name=row[0], name=row[1])
                film.detail_info.douban_rate = row[2]
                film.detail_info.douban_rate_people = row[3]
                film.detail_info.director = row[4]
                film.detail_info.writer = row[5]
                film.detail_info.type_list = row[6].split('/')
                film.detail_info.country = row[7]
                film.detail_info.release_time = row[8]
                film.detail_info.duration = row[9]
                film_query_info_list.append(film)

        return film_query_info_list
