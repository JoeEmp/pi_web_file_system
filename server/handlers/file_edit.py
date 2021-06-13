from tornado.web import RequestHandler, MissingArgumentError
import os
from com.utils import file_info
import logging
from handlers.base_handler import base_handler
from com.pi_error import pi_exception, UNKNOW_ERROR


class file_edit_handler(base_handler):
    def initialize(self, ser=None):
        if not ser:
            self.ser = file_edit_module()
        else:
            self.ser = ser

    def post(self):
        try:
            self.is_login()
            text = self.get_body_argument("text")
            path = self.get_argument('path')
            self.finish(self.ser.edit(path, text))
        except MissingArgumentError as e:
            self.finish({'code': 1, 'msg': '%s不能为空' % e.arg_name})
        except pi_exception as e:
            self.finish(e.reason)
        except Exception as e:
            logging.error(e)
            self.finish(UNKNOW_ERROR)


class file_edit_module():

    def edit(self, path, text):
        try:
            if not os.path.exists(path):
                raise FileNotFoundError
            with open(path, 'w') as f:
                f.write(text)
            return dict(code=0)
        except FileNotFoundError as e:
            return dict(code=-1, msg='文件不存在')
        except PermissionError as e:
            return dict(code=2, msg="权限不足")
