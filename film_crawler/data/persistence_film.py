#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import csv
from . import FilmQueryInfo
from film_crawler.base import logger


class PersistenceFilmQueryInfo(object):
    @staticmethod
    def save_to_file(film_query_info_list, filename):
        with open(filename, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file, lineterminator='\r\n')

            for item in film_query_info_list:
                try:
                    writer.writerow([item.origin_name,
                                     item.name,
                                     item.detail_info.douban_rate,
                                     item.detail_info.douban_rate_people,
                                     '/'.join(item.detail_info.director_list),
                                     '/'.join(item.detail_info.writer_list),
                                     '/'.join(item.detail_info.cast_list),
                                     '/'.join(item.detail_info.type_list),
                                     '/'.join(item.detail_info.country_list),
                                     '/'.join(item.detail_info.release_time_list),
                                     '/'.join(item.detail_info.duration_list)])
                except UnicodeEncodeError:
                    pass
                except Exception as e:
                    logger.warn(e)

    @staticmethod
    def load_from_file(filename):
        film_query_info_list = []
        with open(filename, encoding='utf-8') as file:
            reader = csv.reader(file, lineterminator='\r\n')
            for row in reader:
                film = FilmQueryInfo(origin_name=row[0], name=row[1])
                film.detail_info.douban_rate = row[2]
                film.detail_info.douban_rate_people = row[3]
                film.detail_info.director_list = row[4].split('/')
                film.detail_info.writer_list = row[5].split('/')
                film.detail_info.cast_list = row[6].split('/')
                film.detail_info.type_list = row[7].split('/')
                film.detail_info.country_list = row[8].split('/')
                film.detail_info.release_time_list = row[9].split('/')
                film.detail_info.duration_list = row[10].split('/')
                film_query_info_list.append(film)

        return film_query_info_list
