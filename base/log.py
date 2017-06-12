#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import logging

logger = logging.getLogger('film_crawler')

formatter = logging.Formatter('[%(asctime)s] %(message)s', '%H:%M:%S')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
file_handler = logging.FileHandler('film_crawlers.log', mode='w')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)