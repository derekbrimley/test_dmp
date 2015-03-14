# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425796529.721138
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp/base_app/templates/base.htm'
_template_uri = '/base_app/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['nav', 'account', 'content', 'header', 'footer']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def nav():
            return render_nav(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def account():
            return render_account(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n\t<meta charset="UTF-8">\r\n\t<head>\r\n\r\n\t<title>homepage</title>\r\n\r\n')
        __M_writer('\t<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n\t<link rel="icon" type="image/x-icon" href="\\static\\homepage\\media\\favicon.ico" />\r\n\t<link href=\'http://fonts.googleapis.com/css?family=Roboto:100\' rel=\'stylesheet\' type=\'text/css\'>\r\n\t<script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('base_app/media/jquery.loadmodal.js"></script>\r\n\t<script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('base_app/media/jquery.form.js"></script>\r\n')
        __M_writer('\t')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n\t</head>\r\n\t<body>\r\n\t\t<div class="wrapper">\r\n\t\t\t<div class="header">\r\n\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\t\t\t</div>\r\n\t\t\t<div class="container-fluid"\r\n\t\t\t\t<div class="row">\r\n\t\t\t\t\t<div class="col-md-2 left-menu">\r\n\t\t\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav'):
            context['self'].nav(**pageargs)
        

        __M_writer('\r\n\t\t\t\t\t</div>\t\r\n\t\t\t\t\t<div class="col-md-8 content">\t\r\n\t\t\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<div class="col-md-2">\r\n\t\t\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'account'):
            context['self'].account(**pageargs)
        

        __M_writer('\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t\t<nav class="nav-bar navbar-default navbar-fixed-bottom">\r\n\t\t\t\t<div class="container-fluid">\r\n\t\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\r\n\t\t\t\t</div>\r\n\t\t\t</nav>\r\n\t\t</div>\r\n\t</body>\t\r\n</html>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def nav():
            return render_nav(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t\t\t\t\t\tNAVIGATION BAR\r\n\t\t\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_account(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def account():
            return render_account(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.is_authenticated():
            __M_writer('\t\t\t\t\t\t\t\t\t<a href="/account/" class="btn btn-default" aria-label="Right Align">\r\n\t\t\t\t\t\t\t\t\t\t<span class="glyphicon glyphicon-home" aria-hidden="true"/>\r\n\t\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t<span class="label label-primary"/>Account Home\r\n\t\t\t\t\t\t\t\t<br/>\r\n\t\t\t\t\t\t\t\t<br/>\r\n\t\t\t\t\t\t\t\t<a href="/account/logout/">\r\n\t\t\t\t\t\t\t\t\t<button class="btn btn-default" action="/account/logout/" aria-label="Right Align">\r\n\t\t\t\t\t\t\t\t\t\t<span class="glyphicon glyphicon-user" aria-hidden="true"/>\r\n\t\t\t\t\t\t\t\t\t</button>\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t<span class="label label-primary"/> Sign Out\r\n')
        else:
            __M_writer('\t\t\t\t\t\t\t\t<button id="show_login_dialog" class="btn btn-default" aria-label="Right Align">\r\n\t\t\t\t\t\t\t\t\t<span class="glyphicon glyphicon-user" aria-hidden="true"></span>\r\n\t\t\t\t\t\t\t\t</button>\r\n\t\t\t\t\t\t\t\t<span class="label label-danger">My Account</span>\r\n')
        __M_writer('\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t')
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


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        request = context.get('request', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"65": 45, "107": 68, "132": 29, "133": 31, "70": 69, "113": 44, "136": 32, "137": 34, "75": 77, "76": 85, "77": 85, "143": 75, "16": 4, "18": 0, "83": 39, "149": 75, "89": 39, "155": 149, "135": 32, "125": 29, "95": 48, "36": 2, "37": 4, "38": 5, "103": 49, "104": 50, "105": 62, "42": 5, "43": 15, "44": 20, "45": 20, "46": 21, "47": 21, "48": 23, "49": 23, "50": 23, "106": 63, "55": 34, "119": 44, "60": 41, "102": 48, "134": 32}, "uri": "/base_app/templates/base.htm", "filename": "C:\\Users\\Derek\\python\\test_dmp/base_app/templates/base.htm"}
__M_END_METADATA
"""
