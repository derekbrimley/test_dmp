# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423368004.752824
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/orders.edit.html'
_template_uri = 'orders.edit.html'
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
        form = context.get('form', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<form class="form-horizontal" method="POST">\r\n')
        for field in form:
            __M_writer('\t\t\t<div class="form-group">\r\n\t\t\t\t<label for=')
            __M_writer(str(field.name))
            __M_writer(' class="col-sm-2">')
            __M_writer(str(field.label))
            __M_writer('</label>\r\n\t\t\t\t<div class="col-sm-10">\r\n\t\t\t\t\t')
            __M_writer(str(field))
            __M_writer('\r\n\t\t\t\t\t')
            __M_writer(str( field.errors ))
            __M_writer('\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n')
        __M_writer('\t\t<br/><button class="btn btn-primary" type="submit">Submit</button>\r\n\t\t<a class="btn btn-danger" href="/homepage/orders/">Cancel</a>\r\n\t</form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "orders.edit.html", "line_map": {"35": 1, "69": 63, "45": 3, "27": 0, "52": 3, "53": 5, "54": 6, "55": 7, "56": 7, "57": 7, "58": 7, "59": 9, "60": 9, "61": 10, "62": 10, "63": 14}, "source_encoding": "ascii", "filename": "C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/orders.edit.html"}
__M_END_METADATA
"""