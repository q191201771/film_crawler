#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import logging

logger = logging.getLogger('film_crawler')

handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(message)s', '%H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)