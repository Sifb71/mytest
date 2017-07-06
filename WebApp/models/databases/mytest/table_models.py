#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
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


class User(PeeweeBaseModel):
    id = PrimaryKeyField()
    email = CharField()
    password = CharField()
    first_name = CharField()
    last_name = CharField()
    status = CharField()  # user status filed contain this value: active, de_active, deleted
    created_at = DateTimeField(default=datetime.datetime.now())


class User_address(PeeweeBaseModel):
    id = PrimaryKeyField()
    address = TextField()
    user = ForeignKeyField(User, to_field=User.id, related_name='user_address')
    street_number = CharField()
    route = CharField()
    locality = CharField()
    street_number2 = CharField()
    country = CharField()
    created_at = DateTimeField(default=datetime.datetime.now())
    is_validate = IntegerField(1)


