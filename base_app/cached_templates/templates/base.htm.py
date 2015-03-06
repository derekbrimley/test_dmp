# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425444164.224459
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\base_app\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'content', 'footer', 'account', 'nav']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def header():
            return render_header(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def account():
            return render_account(context._locals(__M_locals))
        def nav():
            return render_nav(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n\t<meta charset="UTF-8">\r\n\t<head>\r\n\r\n\t<title>homepage</title>\r\n\r\n')
        __M_writer('\t<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\r\n\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\r\n\t<link rel="icon" type="image/x-icon" href="\\static\\homepage\\media\\favicon.ico" />\r\n\t<link href=\'http://fonts.googleapis.com/css?family=Roboto:100\' rel=\'stylesheet\' type=\'text/css\'>\r\n')
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


def render_account(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def account():
            return render_account(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.is_authenticated():
            __M_writer('\t\t\t\t\t\t\t\t<a href="/account/">\r\n\t\t\t\t\t\t\t\t\t<button class="btn btn-default" aria-label="Right Align">\r\n\t\t\t\t\t\t\t\t\t\t<span class="glyphicon glyphicon-home" aria-hidden="true"/>\r\n\t\t\t\t\t\t\t\t\t</button>\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t<span class="label label-primary"/>Account Home\r\n\t\t\t\t\t\t\t\t<br/>\r\n\t\t\t\t\t\t\t\t<br/>\r\n\t\t\t\t\t\t\t\t<a href="/homepage/logout/">\r\n\t\t\t\t\t\t\t\t\t<button class="btn btn-default" aria-label="Right Align">\r\n\t\t\t\t\t\t\t\t\t\t<span class="glyphicon glyphicon-user" aria-hidden="true"/>\r\n\t\t\t\t\t\t\t\t\t</button>\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t<span class="label label-primary"/> Sign Out\r\n')
        else:
            __M_writer('\t\t\t\t\t\t\t\t<a class="login_btn" href="/homepage/login/">\r\n\t\t\t\t\t\t\t\t\t<button class="btn btn-default" aria-label="Right Align">\r\n\t\t\t\t\t\t\t\t\t\t<span class="glyphicon glyphicon-user" aria-hidden="true"></span>\r\n\t\t\t\t\t\t\t\t\t</button>\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t<span class="label label-danger">My Account</span>\r\n')
        __M_writer('\t\t\t\t\t\t')
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


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Derek\\python\\test_dmp\\base_app\\templates/base.htm", "line_map": {"128": 48, "65": 71, "130": 63, "131": 64, "132": 71, "150": 144, "70": 79, "71": 87, "72": 87, "108": 77, "138": 38, "78": 28, "16": 4, "18": 0, "85": 28, "86": 30, "87": 31, "88": 31, "89": 31, "90": 33, "96": 43, "144": 38, "35": 2, "36": 4, "37": 5, "102": 43, "129": 49, "41": 5, "42": 15, "43": 22, "44": 22, "45": 22, "50": 33, "55": 40, "120": 47, "114": 77, "60": 44, "127": 47}, "uri": "base.htm"}
__M_END_METADATA
"""
