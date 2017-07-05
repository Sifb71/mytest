#!/usr/bin/env python
# -*- coding: utf-8 -*-
from WebApp.classes.Debug import Debug
from WebApp.classes.public import CreateHash

__author__ = 'Sifb71'
from WebApp.models.databases.mytest.table_models import *


class SysUser:
    def __init__(self, _id=None, email=None, password=None, first_name=None, last_name=None, status='active',
                 created_at=None):
        self.id = _id
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.created_at = created_at


    def insert(self):
        try:
            self.password = CreateHash.create(self.password)
            x = User.insert(
                email=self.email,
                password=self.password,
                first_name=self.first_name,
                last_name=self.last_name,
                status=self.status,
            ).execute()
            return x if x else False
        except:
            Debug.get_exception()
            return False

    def is_exist(self):
        try:
            if self.email:
                if User.select().where(User.email == self.email).count():
                    return True
            return False
        except:
            Debug.get_exception()
            return False

    def get_one(self):
        try:
            u = User.select().where(User.email == self.email).get()
            return dict(
                id=u.id,
                email=u.email,
                first_name=u.first_name,
                last_name=u.last_name,
                password=u.password
            )
        except:
            Debug.get_exception()
            return dict()


class SysUser_address:
    def __init__(self, id=None, address=None, user=None, created_at=None):
        self.id = id
        self.address = address
        self.user = user
        self.created_at = created_at


    def insert(self):
        try:
            x = User_address.insert(
                address=self.address,
                user=self.user,
                created_at=self.created_at
            ).execute()
            return x if x else False
        except:
            return False

