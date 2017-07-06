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
            if self.email:
                u = User.select().where(User.email == self.email).get()
            else:
                u = User.select().where(User.id == self.id).get()
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

    def update(self, **kwargs):
        try:
            User.update(**kwargs).where(User.id == self.id).execute()
            return True
        except:
            Debug.get_exception()
            return False


class SysUser_address:
    def __init__(self, _id=None, address=None, user=None, created_at=datetime.datetime.now(), street_number=None,
                 route=None,
                 locality=None, street_number2=None, country=None, is_validate=None):
        self.id = _id
        self.address = address
        self.user = user
        self.created_at = created_at
        self.street_number = street_number
        self.route = route
        self.locality = locality
        self.street_number2 = street_number2
        self.country = country
        self.is_validate = is_validate


    def insert(self):
        try:
            x = User_address.insert(
                address=self.address,
                user=self.user,
                created_at=self.created_at,
                street_number=self.street_number,
                route=self.route,
                locality=self.locality,
                street_number2=self.street_number2,
                country=self.country,
                is_validate=self.is_validate
            ).execute()
            return x if x else False
        except:
            Debug.get_exception()
            return False

    def update(self, **kwargs):
        try:
            x = User_address.update(**kwargs).where(User_address.id == self.id).execute()
            return True
        except:
            Debug.get_exception()
            return False

    def update_or_insert(self):
        try:
            a = User_address.select().where(User_address.user == self.user).count()
            if a:
                User_address.update(address=self.address,
                                    created_at=self.created_at,
                                    street_number=self.street_number,
                                    route=self.route,
                                    locality=self.locality,
                                    street_number2=self.street_number2,
                                    country=self.country,
                                    is_validate=self.is_validate).where(User_address.user == self.user).execute()
            else:
                if self.address:
                    self.insert()
        except:
            Debug.get_exception()
            return False

    def get_user_address(self):
        try:
            a = User_address.select().where(User_address.user == self.user).get()
            return dict(
                address=a.address,
                user=a.user,
                street_number=a.street_number,
                route=a.route,
                locality=a.locality,
                street_number2=a.street_number2,
                country=a.country,
                is_validate=a.is_validate
            )
        except:
            return dict(
                address='',
                user='',
                street_number='',
                route='',
                locality='',
                street_number2='',
                country='',
                is_validate=0
            )

    @staticmethod
    def get_all_valid_address(_page=1, _count=10):
        try:
            a = User_address().select(
                User_address.id,
                User.first_name,
                User.last_name,
                User_address.address
            ). \
                join(User, on=User_address.user == User.id). \
                where(User_address.is_validate == 1).naive().paginate(_page,_count)
            ls = []
            for ad in a:
                ls.append(dict(
                    id=ad.id,
                    user_full_name=ad.first_name + u' ' + ad.last_name,
                    address=ad.address
                ))
            return ls

        except:
            Debug.get_exception()
            return []

    @staticmethod
    def get_count_all_valid():
        try:
            return User_address.select().where(User_address.is_validate == 1).count()
        except:
            Debug.get_exception()
            return 0

