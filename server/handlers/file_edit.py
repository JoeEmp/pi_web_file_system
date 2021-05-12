from tornado.web import RequestHandler, MissingArgumentError
from handlers.base_handler import UNKNOW_ERROR
import os
from utils import file_info
import logging


class file_edit_handler(RequestHandler):
    def initialize(self, ser=None):
        if not ser:
            self.ser = file_edit_module()
        else:
            self.ser = ser

    def post(self):
        try:
            text = self.get_argument("text")
            path = self.get_argument('path')
            self.finish(self.ser.edit(path, text))
        except MissingArgumentError as e:
            self.finish({'code': 1, 'msg': '%s不能为空' % e.arg_name})
        except Exception as e:
            logging.error(e)
            self.finish(UNKNOW_ERROR)


class file_edit_module():

    def edit(self, path, text):
        try:
            with open(path, 'w') as f:
                f.write(text)
            return dict(code=0)
        except FileNotFoundError as e:
            return dict(code=-1, msg='文件不存在')
        except PermissionError as e:
            return dict(code=2, msg="权限不足")
