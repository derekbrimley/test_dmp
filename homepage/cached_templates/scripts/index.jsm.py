# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1422330203.114666
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\test_dmp\\homepage\\scripts/index.jsm'
_template_uri = 'index.jsm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer("$(function() {\r\n  // update the time every n seconds\r\n  window.setInterval(function() {\r\n\t$('.browser-time').text('The current browser time is ' + new Date());\r\n  }, ")
        __M_writer(str( request.urlparams[1] ))
        __M_writer(");\r\n\r\n// update button\r\n$('#server-time-button').click(function() {\r\n  $('.server-time').load('/homepage/index.gettime');\r\n});")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Derek\\test_dmp\\homepage\\scripts/index.jsm", "uri": "index.jsm", "line_map": {"16": 0, "24": 5, "30": 24, "22": 1, "23": 5}}
__M_END_METADATA
"""
