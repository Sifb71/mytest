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
    email = CharField(max_length=255)
    password = CharField(max_length=255)
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    status = CharField()  # user status filed contain this value: active, de_active, deleted
    created_at = DateTimeField(default=datetime.datetime.now())


class User_address(PeeweeBaseModel):
    id = PrimaryKeyField()
    address = TextField()
    user = ForeignKeyField(User, to_field=User.id, related_name='user_address')
    street_number = CharField(max_length=100)
    route = CharField(max_length=100)
    locality = CharField(max_length=100)
    street_number2 = CharField(max_length=100)
    country = CharField(max_length=100)
    created_at = DateTimeField(default=datetime.datetime.now())
    is_validate = IntegerField(1)


