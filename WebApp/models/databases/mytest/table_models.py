#!/usr/bin/env python
# -*- coding: utf-8 -*-
from peewee import PrimaryKeyField

__author__ = 'Sifb71'
from peewee import *
from config import Config

sh = Config()

web_db = MySQLDatabase(
    database=sh.web['mysql']['db'],
    host=sh.web['mysql']['host'],
    user=sh.web['mysql']['user'],
    passwd=sh.web['mysql']['password'],
    charset="utf8"
)


class PeeweeBaseModel(Model):
    class Meta:
        database = web_db

