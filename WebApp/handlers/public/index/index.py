#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado import gen


__author__ = 'Sifb71'

from WebApp.handlers.base import WebBaseHandler


class IndexHandler(WebBaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.data['title'] = 'Test Start Page'
        self.render("base/public/index/index.html", **self.data)


