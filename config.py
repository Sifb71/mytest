#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sifb71'

import os


class Config:
    def __init__(self):
        self.applications_root = os.path.join(os.path.dirname(__file__), "")
        self.domain = '.localhost'
        self.project_path = os.path.dirname(__file__)

        self.SESSION_TIME = 86400

        self.mobile = {
            'port': 8081,
            'redis': {
                'host': '127.0.0.1', 'port': 6379, 'db': 3, 'password': '1234567890 0987654321foo'
            }
        }

        self.web = {
            'port': 8080,
            'server_ip': '127.0.0.1',
            'server_path': os.path.join(self.applications_root, 'WebApp/'),
            'mysql': {
                'host': '127.0.0.1',
                'db': 'mytest',
                'user': 'root',
                'password': '',
                'port': 3306,
            },
            'redis': {
                'password': '',
            },
            'template_address': os.path.join(os.path.dirname(__file__), "WebApp", "templates"),
            'static_address': os.path.join(os.path.dirname(__file__), "static"),
        }

        self.global_config = {
            'cookie_secret': "Gy8tgGsVwhber82huaIY*TG$Ub3u9rh-7dwg4u23;86^t&T4PY32Y&sAl",
            'login_url': 'http://{0}:{1}/login'.format(self.web['server_ip'], self.web['port']),
            'logout_url': 'http://{0}:{1}/logout'.format(self.web['server_ip'], self.web['port']),
            'redis': {
                'host': '127.0.0.1',
                'port': 6379,
                'password': "",
                'db_sessions': 8,
                'db_notifications': 9,
            },
        }