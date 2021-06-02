from tornado.web import RequestHandler, MissingArgumentError
import os

class index_handler(RequestHandler):

    def get(self):
        self.finish("<h1>Hello</h1>")