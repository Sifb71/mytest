#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from tornado import gen
from WebApp.classes.public import CreateHash
from WebApp.models.main.base_model import SysUser


__author__ = 'Sifb71'

from WebApp.handlers.base import WebBaseHandler, authentication


class UserProfileHandler(WebBaseHandler):
    @authentication()
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.data['title'] = "My Profile"
        self.data['user'] = SysUser(_id=self.current_user).get_one()
        self.data['message'] = self.session.get('message')
        self.session.set('message', None)
        self.render("base/users/profile/profile.html", **self.data)
    @authentication()
    @gen.coroutine
    def post(self, *args, **kwargs):
        email = self.get_argument('email', '')
        first_name = self.get_argument('first_name', '')
        last_name = self.get_argument('last_name', '')
        password = self.get_argument('password', '')
        if email and first_name and last_name:
            __data = dict()
            __data['first_name'] = first_name
            __data['last_name'] = last_name
            u = SysUser(email=email).get_one()
            if u['email'] != email:
                if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
                    self.errors.append('Your email address is incorrect.')
                else:
                    __data['email'] = email
            if password:
                if len(password) < 5:
                    self.errors.append('Password must be at least 5 character.')
                else:
                    __data['password'] = CreateHash().create(password)
            if not self.errors:
                SysUser(_id=self.current_user).update(**__data)
                self.session.set('message', dict(type='message', value=['Your change saved']))
        else:
            self.errors.append('Please enter all parameter.')
        if self.errors:
            self.session.set('message', dict(type='errors', value=self.errors))
        self.redirect(self.reverse_url('u:MyProfile'))
