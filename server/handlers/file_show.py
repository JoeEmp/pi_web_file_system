from tornado.web import RequestHandler, MissingArgumentError
import os
from com.utils import file_info
from com.pi_error import pi_exception, UNKNOW_ERROR
from handlers.base_handler import base_handler
import logging


class file_show_handler(base_handler):
    def initialize(self, ser=None):
        if not ser:
            self.ser = file_show_module(self.request.uri.replace('/file', ''))
        else:
            self.ser = ser

    def get(self):
        try:
            self.is_login()
            self.finish(self.ser.show())
        except pi_exception as e:
            self.finish(e.reason)
        except Exception as e:
            logging.error(e)
            self.finish(UNKNOW_ERROR)


class file_show_module():
    def __init__(self, path):
        if not path:
            path = '/'
        self.path = path

    def show(self):
        try:
            target_files = []
            for file in os.listdir(self.path):
                file = os.path.join(self.path, file)
                target_files.append(
                    file_info(file, user='root')
                )
            return dict(code=0, list=target_files)
        except Exception as e:
            return {'code': -1, 'msg': '目录不存在'}
