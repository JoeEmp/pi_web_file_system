from tornado.web import MissingArgumentError
from handlers.base_handler import base_handler
import logging
from com.utils import gen_token, sync_token
from com.pi_error import UNKNOW_ERROR
from settings import USERNAME, PASSWORD


class login_handler(base_handler):
    def post(self):
        try:
            username = self.get_body_argument('username')
            password = self.get_body_argument('password')
            self.finish(self.login(username, password))
        except MissingArgumentError as e:
            self.finish(self.warn_tips(msg='%s不能为空' % e.arg_name))
        except Exception as e:
            logging.error(e)
            self.finish(UNKNOW_ERROR)

    def login(self, username, password):
        """return token or error msg. """
        if username == USERNAME and password == PASSWORD:
            return self.base_tips(token=gen_token(username))
        elif username == USERNAME:
            return self.warn_tips(msg="不存在该用户")
        elif password == PASSWORD:
            return self.warn_tips(msg="密码错误")
        else:
            return UNKNOW_ERROR
