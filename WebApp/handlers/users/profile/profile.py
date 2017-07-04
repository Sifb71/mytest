#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from tornado import gen
from WebApp.classes.public import CreateRandom, CreateHash
from WebApp.models.main.base_model import SysUsers, SysActiveCode
from WebApp.models.main.ticket.ticket import SysTicket, SysTicketText

__author__ = 'Sifb71'

from WebApp.handlers.base import WebBaseHandler, authentication


class UserDashboardHandler(WebBaseHandler):
    @authentication()
    @gen.coroutine
    def get(self, *args, **kwargs):
        self.data['title'] = "My Profile"
        self.render("base/users/profile/profile.html", **self.data)