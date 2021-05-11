from tornado.web import RequestHandler, MissingArgumentError
import os
from utils import file_info
import logging


class file_read_handler(RequestHandler):
    def initialize(self, ser=None):
        if not ser:
            self.ser = file_read_module()
        else:
            self.ser = ser

    def post(self):
        try:
            path = self.get_argument('path')
            self.finish(self.ser.read(path))
        except MissingArgumentError as e:
            self.finish({'code': 1, 'msg': '%s不能为空' % e.arg_name})
        except Exception as e:
            logging.error(e)
            self.finish({"code": -1, 'msg': '未知错误'})


class file_read_module():

    def read(self, path):
        try:
            with open(path, 'r') as f:
                return dict(code=0, text=f.read())
        except FileNotFoundError as e:
            return dict(code=-1, msg='文件不存在')
        except PermissionError as e:
            return dict(code=2, msg="权限不足")
