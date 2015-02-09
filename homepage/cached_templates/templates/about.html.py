# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423018559.815788
_enable_loop = True
_template_filename = 'C:\\users\\derek\\python\\test_dmp\\homepage\\templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'header']


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
        def header():
            return render_header(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

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
        __M_writer("\r\n\t<h1>The Colonial Heritage Foundation</h1>\r\n\t<p>\r\n\t\tThe Colonial Heritage Foundation (the Foundation) is a 501(c)(3) \r\n\t\tcorporation dedicated to the preservation of the values, culture, \r\n\t\tskills and history of America's founding. To accomplish this mission, \r\n\t\tthe Foundation engages in a broad array of activities. Among these are \r\n\t\tthe development and presentation of educational exhibits, the coordination \r\n\t\tof reading and discussion groups to encourage the study of America's \r\n\t\thistorical writings, the presentation of lectures and seminars regarding \r\n\t\tAmerica's founding era, the coordination of historical reenactments and \r\n\t\tskill demonstrations, and the coordination of internships and \r\n\t\tapprenticeships that teach the occupational skills of early America.\r\n\t</p>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n\tAbout the Colonial Heritage Foundation\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"75": 69, "51": 7, "36": 1, "69": 3, "57": 7, "41": 5, "27": 0, "63": 3}, "source_encoding": "ascii", "uri": "about.html", "filename": "C:\\users\\derek\\python\\test_dmp\\homepage\\templates/about.html"}
__M_END_METADATA
"""
