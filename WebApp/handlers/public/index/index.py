#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from tornado import gen
from WebApp.classes.permissions import user_permissions
from WebApp.classes.public import RenderToNotificationHtml, CreateHash
from WebApp.models.main.base_model import SysUser


__author__ = 'Sifb71'

from WebApp.handlers.base import WebBaseHandler


class IndexHandler(WebBaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.data['title'] = 'Test Start Page'
        if not self.current_user:
            self.render("base/public/index/index.html", **self.data)
        else:
            self.redirect(self.reverse_url('u:MyProfile'))

    @gen.coroutine
    def post(self, *args, **kwargs):
        _type = self.get_argument('type', '')
        email = self.get_argument('email', '')
        password = self.get_argument('password', '')
        if _type == 'login':
            self.data['form_type'] = 'login'  # flag for display errors in landing page
            if email and password:
                u = SysUser(email=email).get_one()
                if u:
                    if CreateHash.create(password) == u['password']:
                        self.session.set("current_user", u['id'])
                        self.session.set("full_name", u['first_name'] + u' ' + u['last_name'])
                        self.session.set('user_permissions', user_permissions.user_permission)
                        self.redirect(self.reverse_url("u:MyProfile"))
                        return
                self.errors.append('Username or password incorrect.')
            else:
                self.errors.append('Please enter all parameters')

        else:
            first_name = self.get_argument('first_name', '')
            last_name = self.get_argument('last_name', '')
            re_password = self.get_argument('re_password', '')
            self.data['form_type'] = 'signup'  # flag for display errors in landing page
            if email and first_name and last_name and password and re_password:
                pass
            else:
                self.errors.append('Please Enter All Parameter.')
            if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
                self.errors.append('Your email address is incorrect.')

            if SysUser(email=email).is_exist():
                self.errors.append('The email is already exist.')
            if password != re_password:
                self.errors.append('Password does not match the confirm password.')
            elif len(password) < 5:
                self.errors.append('Password must be at least 5 character.')

            if not self.errors:
                u = SysUser(email=email, first_name=first_name, last_name=last_name, password=password).insert()
                if u:
                    self.session.set("current_user", u)
                    self.session.set("full_name", first_name + u' ' + last_name)
                    self.session.set('user_permissions', user_permissions.user_permission)
                    self.redirect(self.reverse_url("u:MyProfile"))
                    return
                else:
                    self.errors.append('One error occurred, please try again.')

        self.render("base/public/index/index.html", **self.data)



class LogoutHandler(WebBaseHandler):
    def get(self):
        for i in self.session.keys():
            self.session.delete(i)
        self.redirect(self.reverse_url('index'))





