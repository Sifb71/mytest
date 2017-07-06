#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from tornado import gen
from WebApp.models.main.base_model import SysUser_address


__author__ = 'Sifb71'

from WebApp.handlers.base import WebBaseHandler, authentication


class UserAddressListHandler(WebBaseHandler):
    @authentication()
    @gen.coroutine
    def get(self,_page, *args, **kwargs):
        try:
            _page =int(_page)
            if _page < 1:
                _page=1
        except:
            _page = 1
        self.data['title'] = "Valid Address List"
        self.data['address'] = SysUser_address.get_all_valid_address(_page)
        self.data['count_all'] = SysUser_address.get_count_all_valid()
        self.data['page'] = _page
        self.render("base/users/address_list/address_list.html", **self.data)