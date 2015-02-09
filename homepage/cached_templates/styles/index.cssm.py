# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423369785.755514
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\homepage\\styles/index.cssm'
_template_uri = 'index.cssm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(".server-time {\r\n\tfont-size: 2em;\r\n\tcolor: red;\r\n}\r\n\r\n@font-face {\r\n    font-family: 'Milano';\r\n    src: 'styles/Milano_regular.ttf';\r\n}\r\n\t\r\nhtml, body {\r\n\theight: 100%;\r\n\tmargin: 0;\r\n\tpadding: 0;\r\n\tpadding-bottom: 70px;\r\n}\r\n\r\n.header {\r\n\tfont-family: 'Roboto', sans-serif;\r\n\tpadding-left: 15px;\r\n\tpadding-top: 20px;\r\n\tpadding-bottom: 20px;\r\n\ttext-align: left;\r\n\tfont-size: 3.5em;\r\n\tcolor: #F4F4F4;\r\n\tbackground-color: #800000;\r\n\tborder-bottom: 50px;\r\n}\r\n\r\n.footer{\r\n\tfont-family: 'Roboto', sans-serif;\r\n\ttext-align: right;\r\n\twidth:100%;\r\n\theight:30px;\r\n\tposition:absolute;\r\n\tbottom:0;\r\n\tleft:0;\r\n\tbackground:lightgray;\r\n}\r\n\r\n.content{\r\n\tfont-family: 'Roboto', sans-serif;\r\n\tpadding-top:30px;\r\n\tpadding-left:50px;\r\n}\r\n\r\n.col-md-3{\r\n\tfont-family: 'Roboto', sans-serif;\r\n\tpadding-top: 5px;\r\n}\r\n\r\n.dropdown{\r\n\tpadding-bottom: 5px;\r\n}\r\n\r\n.btn-primary{\r\n}\r\n\r\n.btn-success{\r\n}\r\n\r\n.glyphicon-user{\r\n\talign-content: right;\r\n}\r\n\r\n.col-md-2{\r\nfont-family: 'Roboto', sans-serif;\r\n\tpadding-top: 15px;\r\n}\r\n\r\n.btn-default{\r\n}\r\n\r\n.left-menu{\r\n\tbackground-color: lightgray;\r\n}\r\n\r\n.container-fluid{\r\n\tfont-family: 'Roboto', sans-serif;\r\n}")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.cssm", "filename": "C:\\Users\\Derek\\python\\test_dmp\\homepage\\styles/index.cssm", "source_encoding": "ascii", "line_map": {"16": 0, "27": 21, "21": 1}}
__M_END_METADATA
"""
