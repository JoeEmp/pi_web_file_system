from handlers.file_show import file_show_handler
from handlers.file_edit import file_edit_handler
from handlers.file_read import file_read_handler
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado import options
from tornado.options import define, options
import os

PORT = 10086

url_patterns = [
    (r'/file/.+?', file_show_handler),
    (r'/file', file_show_handler),
    (r'/edit', file_edit_handler),
    (r'/read', file_read_handler)
]


def make_app(is_debug=False):
    return Application(
        url_patterns,
        template_path=os.path.join(os.path.abspath(
            os.path.dirname(__file__)), 'templates'),
        debug=is_debug
    )


def main():
    app = make_app()
    options.parse_command_line()
    http_server = HTTPServer(app, xheaders=True)
    http_server.listen(options.port)
    IOLoop.instance().start()


def debug_main():
    app = make_app(is_debug=True)
    app.listen(PORT)
    IOLoop.current().start()
    print('start server')
    print('-'*80)


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2 and sys.argv[1] == 'debug':
        debug_main()
    else:
        main()
