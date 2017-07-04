#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Sifb71'
from WebApp.handlers.users.profile import profile
from WebApp.handlers.users.address_list import address

urls = [
    (r'^(?i)/MyProfile[/]?([\d^/]+)?[/]?$', profile.UserProfileHandler),
    (r'/MyProfile', profile.UserProfileHandler , None, "MyProfile"),

    (r'^(?i)/AddressList[/]?([\d^/]+)?[/]?$', address.UserAddressListHandler),
    (r'/AddressList', address.UserAddressListHandler , None, "AddressList"),


]
