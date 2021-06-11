from tornado.web import RequestHandler
from com.utils import sync_token
from com.pi_error import pi_exception, LOGIN_ERROR
from settings import USERNAME
from time import time


class base_handler(RequestHandler):
    def finish(self, chunk=None):
        if isinstance(chunk, dict):
            self.set_header('Content-type', 'application/json; charset=utf-8')
        return super().finish(chunk=chunk)

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*") 
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        return super().set_default_headers()

    def is_login(self):
        """return payload or raise pi_exception use handler error """
        token = self.request.headers.get('token', None)
        if token:
            ret = sync_token(token)
            if ret.get('exp', 0) > time() and self.is_legal_user(ret.get('username', '')):
                ret['code'] = 0
                return ret
        raise pi_exception(LOGIN_ERROR)

    def is_legal_user(self, username):
        return True if username == USERNAME else False

    def error_tips(self, **kwargs):
        return self.tips(-1, **kwargs)

    def warn_tips(self, **kwargs):
        return self.tips(1, **kwargs)

    def base_tips(self, **kwargs):
        return self.tips(0, **kwargs)

    def redirect_tips(self, **kwargs):
        return self.tips(2, **kwargs)

    def tips(self, code, **kwargs):
        return {'code': code, **kwargs}
