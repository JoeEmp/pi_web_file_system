from handlers.file_show import file_show_handler
from handlers.file_edit import file_edit_handler
from handlers.file_read import file_read_handler
from handlers.index import index_handler

url_patterns = [
    (r'/file.+?', file_show_handler),
    (r'/file', file_show_handler),
    (r'/edit', file_edit_handler),
    (r'/read', file_read_handler),
    (r'/', index_handler)
]
