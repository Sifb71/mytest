#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sifb71'
from WebApp.urls import public, users

url_patterns = public.urls + users.urls
