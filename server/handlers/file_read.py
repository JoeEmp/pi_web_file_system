from handlers.base_handler import base_handler
from com.pi_error import pi_exception, UNKNOW_ERROR
from tornado.web import MissingArgumentError
import os
from com.utils import file_info
import logging


class file_read_handler(base_handler):
    def initialize(self, ser=None):
        if not ser:
            self.ser = file_read_module()
        else:
            self.ser = ser

    def post(self):
        try:
            self.is_login()
            path = self.get_argument('path')
            self.finish(self.ser.read(path))
        except MissingArgumentError as e:
            self.finish({'code': 1, 'msg': '%s不能为空' % e.arg_name})
        except pi_exception as e:
            self.finish(e.reason)
        except IsADirectoryError as e:
            self.finish(self.warn_tips(msg='目录无法读取'))
        except Exception as e:
            logging.error(type(e))
            self.finish(UNKNOW_ERROR)


class file_read_module():

    def read(self, path):
        try:
            with open(path, 'r') as f:
                return dict(code=0, text=f.read())
        except FileNotFoundError as e:
            return dict(code=-1, msg='文件不存在')
        except PermissionError as e:
            return dict(code=2, msg="权限不足")
