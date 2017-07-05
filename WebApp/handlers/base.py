#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import re
import datetime

import tornado.web

from tornado import gen
from WebApp.models.databases.mytest.table_models import web_db
from pycket.session import SessionMixin
from pycket.notification import NotificationMixin
from config import Config

s = Config()



def authentication():
    def f(func):
        @functools.wraps(func)
        def func_wrapper(self, *args, **kwargs):
            if not self.is_authenticated():
                self.redirect(self.reverse_url("index"))
                return
            try:
                if self.__class__.__name__ not in self.get_user_permissions():
                    self.render(s.web['template_address'] + "/base/notifications/access_denied.html")
                    return
            except Exception as e:
                print (e)
                pass

            return func(self, *args, **kwargs)

        return func_wrapper

    return f

class BaseHandler(tornado.web.RequestHandler, SessionMixin, NotificationMixin):
    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def get_current_user(self):
        return self.session.get('current_user')

    def is_authenticated(self):
        if self.get_current_user() is not None:
            return True
        return False

    def get_user_permissions(self):
        return self.session.get('user_permissions')

    @staticmethod
    def valid_url(url):
        temp = re.sub("[/||\|&|+|,|:|;|=|?|@|#|||'|<|>|.|-|^|*|(|)|%|!|$]", "", url)
        return re.sub(" ", "_", temp)


class WebBaseHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(WebBaseHandler, self).__init__(application, request, **kwargs)
        self.data = dict(
            title="",
            me=None,
            )
        self.errors = []

def on_finish(self):
        pass

def error_handler(self, status_code, **kwargs):
    if status_code == 404:
        self.render("base/notifications/404.html")
    else:
        self.render("base/notifications/error_page.html")



tornado.web.RequestHandler.write_error = error_handler
