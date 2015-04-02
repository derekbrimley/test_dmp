# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427947204.580946
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/batch_processes.html'
_template_uri = 'batch_processes.html'
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
        __M_writer('\r\n\t<h1>Batch Processes</h1><br/>\r\n\t\r\n\t<a href="/homepage/batch_processes.overdue_rentals/">\r\n\t\t<button class="btn btn-primary">\r\n\t\t\tAll Overdue Rentals\r\n\t\t</button>\r\n\t</a>\r\n\t<a href="/homepage/batch_processes.over_30/">\r\n\t\t<button class="btn btn-primary">\r\n\t\t\t30 Days Overdue\r\n\t\t</button>\r\n\t</a>\r\n\t<a href="/homepage/batch_processes.over_60/">\r\n\t\t<button class="btn btn-primary">\r\n\t\t\t60 Days Overdue\r\n\t\t</button>\r\n\t</a>\r\n\t<a href="/homepage/batch_processes.over_90/">\r\n\t\t<button class="btn btn-primary">\r\n\t\t\t90 Days Overdue\r\n\t\t</button>\r\n\t</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/batch_processes.html", "line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "uri": "batch_processes.html"}
__M_END_METADATA
"""
