from tornado.web import RequestHandler, MissingArgumentError
import os
from utils import file_info


class file_show_handler(RequestHandler):
    def initialize(self, ser=None):
        if not ser:
            self.ser = file_show_module(self.request.uri.replace('/file', ''))
        else:
            self.ser = ser

    def get(self):
        # print(__file__)
        # if self.request.uri.replace('/file', '') in os.path.abspath(os.path.dirname(__file__)):
        #     self.finish({'code':-1,"msg":'can\'t edit project dir'})
        # else:
        self.finish(self.ser.show())


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
            return {'code':-1,'msg':'dir not found'}
