#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from tornado import gen


__author__ = 'Sifb71'

from WebApp.handlers.base import WebBaseHandler, authentication


class UserProfileHandler(WebBaseHandler):
    @authentication()
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.data['title'] = "My Profile"
        self.render("base/users/profile/profile.html", **self.data)