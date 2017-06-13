#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author chef <191201771@qq.com>
# @brief  xxx

from .film import FilmQueryInfo, FilmDownloadInfo
from .persistence_film import PersistenceFilmQueryInfo

__all__ = ['FilmQueryInfo', 'FilmDownloadInfo', 'PersistenceFilmQueryInfo']