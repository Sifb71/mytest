import hashlib
import random
from pip import exceptions

__author__ = 'Sifb71'


class RenderToNotificationHtml():
    def __init__(self, handler=None):
        self.handler = handler

    def error_page(self):
        self.handler.render("base/notifications/error_page.html")


class CreateHash():
    def __init__(self):
        pass

    @staticmethod
    def create(password):
        ps = hashlib.md5()
        ps.update(password)
        _hash = ps.hexdigest()
        _hash += ps.hexdigest()[:18:-1]
        _hash = _hash[::-1]
        ps = hashlib.new('ripemd160')
        ps.update(_hash)
        return ps.hexdigest()[7:35]

    @staticmethod
    def create_user_file(_id):
        m = hashlib.md5()
        m.update(str(_id))
        return m.hexdigest()[5:11] + '' + str(_id)

    @staticmethod
    def create_file_name():
        _m = str(random.randint(100000000000000000, 999999999999999999999))
        ps = hashlib.sha1()
        ps.update(_m)
        return ps.hexdigest()[5:20]

    @staticmethod
    def create_download_link():
        try:
            _m = str(random.randint(1236521478965410235, 1459999999999999999999))
            ps = hashlib.sha1()
            ps.update(_m)
            return ps.hexdigest()[0:5] + '/' + ps.hexdigest()[11:22]

        except exceptions as e:
            print (e)
        return False
