#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

import time, random


class Helper(object):
    @staticmethod
    def sleep_uniform(l, r):
        time.sleep(random.uniform(l, r))