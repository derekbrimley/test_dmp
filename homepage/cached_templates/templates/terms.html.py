# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423367171.480167
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/Terms.html'
_template_uri = 'Terms.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Terms of Service</h1>\r\n\t<p>\r\n\t\tThe name "Colonial Heritage Foundation" is \r\n\t\tanother name for the Society for the Preservation \r\n\t\tof America\'s Founding Values, Inc., which is a 501(3)(c) \r\n\t\tpublic charity.\r\n\t</p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/Terms.html", "uri": "Terms.html", "source_encoding": "ascii", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}}
__M_END_METADATA
"""
