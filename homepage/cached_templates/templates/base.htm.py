# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423349556.287207
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['footer', 'header', 'content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def footer():
            return render_footer(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n\t<meta charset="UTF-8">\r\n\t<head>\r\n\r\n\t<title>homepage</title>\r\n\r\n')
        __M_writer('\t<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n\t<link rel="icon" type="image/x-icon" href="\\static\\homepage\\media\\favicon.ico" />\r\n\t<link href=\'http://fonts.googleapis.com/css?family=Roboto:100\' rel=\'stylesheet\' type=\'text/css\'>\r\n\t\r\n')
        __M_writer('\t')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n\t</head>\r\n\t<body>\r\n\t\t<div class="wrapper">\r\n\t\t\t<div class="header">\r\n\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\t\t\t</div>\r\n\t\t\t<div class="container-fluid"\r\n\t\t\t\t<div class="row">\r\n\t\t\t\t\t<div class="col-md-2 left-menu">\r\n\t\t\t\t\t\t<div class="sidebar-nav">\r\n\t\t\t\t\t\t  <ul class="nav nav-pills nav-stacked">\r\n\t\t\t\t\t\t\t<li role="presentation" class="active">\r\n\t\t\t\t\t\t\t<a href="/homepage/">\r\n\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-home" aria-hidden="true"></span> Home\r\n\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t<a href="/homepage/products/">\r\n\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-gift" aria-hidden="true"></span> Products\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</li>\r\n')
        if request.user.has_perm('homepage.is_manager'):
            __M_writer('\t\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t\t<a href="/homepage/items/">\r\n\t\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-th-list" aria-hidden="true"></span> Items\r\n\t\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t\t<a href="/homepage/users/">\r\n\t\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-user" aria-hidden="true"></span> Users\r\n\t\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t\t<a href="/homepage/rentals/">\r\n\t\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-time" aria-hidden="true"></span> Rentals\r\n\t\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t<a href="/homepage/orders/">\r\n\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span> Orders\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t</li>\r\n')
        __M_writer('\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t<a href="/homepage/events/">\r\n\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-calendar" aria-hidden="true"></span> Events\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t<a href="/homepage/about/">\r\n\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-bullhorn" aria-hidden="true"></span> About Us\t\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t<a href="/homepage/contact/">\r\n\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-comment" aria-hidden="true"></span> Contact\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t<a href="/homepage/Terms/">\r\n\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-th" aria-hidden="true"></span> Terms\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t  </ul>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</div>\t\r\n\t\t\t\t\t<div class="col-md-8 content">\t\r\n\t\t\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<div class="col-md-2">\r\n')
        if request.user.is_authenticated():
            __M_writer('\t\t\t\t\t\t\t<a href="/homepage/logout/">\r\n\t\t\t\t\t\t\t\t<button class="btn btn-default" aria-label="Right Align">\r\n\t\t\t\t\t\t\t\t\t<span class="glyphicon glyphicon-user" aria-hidden="true"></span>\r\n\t\t\t\t\t\t\t\t</button>\r\n\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t<span class="label label-primary">Sign Out</span>\r\n')
        else:
            __M_writer('\t\t\t\t\t\t\t<a href="/homepage/login/">\r\n\t\t\t\t\t\t\t\t<button class="btn btn-default" aria-label="Right Align">\r\n\t\t\t\t\t\t\t\t\t<span class="glyphicon glyphicon-user" aria-hidden="true"></span>\r\n\t\t\t\t\t\t\t\t</button>\r\n\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t<span class="label label-danger">Sign In</span>\r\n')
        __M_writer('\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\r\n\t\t\t<nav class="nav-bar navbar-default navbar-fixed-bottom">\r\n\t\t\t\t<div class="container-fluid">\r\n\t\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\r\n\t\t\t\t</div>\r\n\t\t\t</nav>\r\n\t\t</div>\r\n\t</body>\r\n</html>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t\t\t\t\tSite by Derek Brimley\r\n\t\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t\t\t\tThe Colonial Heritage Foundation\r\n')
        if request.user.is_authenticated():
            __M_writer('\t\t\t\t\t\t<span class="welcome">Welcome, ')
            __M_writer(str(request.user.first_name))
            __M_writer('</span>\r\n')
        __M_writer('\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "base.htm", "filename": "C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/base.htm", "line_map": {"64": 123, "65": 131, "66": 131, "72": 121, "96": 33, "78": 121, "16": 4, "18": 0, "84": 28, "91": 28, "92": 30, "93": 31, "94": 31, "31": 2, "32": 4, "33": 5, "37": 5, "38": 15, "39": 22, "40": 22, "41": 22, "95": 31, "108": 96, "46": 33, "47": 50, "48": 51, "49": 72, "114": 108, "54": 97, "55": 100, "56": 101, "57": 107, "58": 108, "59": 115, "102": 96}}
__M_END_METADATA
"""
