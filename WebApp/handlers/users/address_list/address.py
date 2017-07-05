#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from tornado import gen


__author__ = 'Sifb71'

from WebApp.handlers.base import WebBaseHandler, authentication


class UserAddressListHandler(WebBaseHandler):
    @authentication()
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.data['title'] = "Valid Address List"
        self.render("base/users/address_list/address_list.html", **self.data)