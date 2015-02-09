# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423503952.383336
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\Documents\\GitHub\\CHF\\test_dmp\\homepage\\templates/products.edit.html'
_template_uri = 'products.edit.html'
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
        form = context.get('form', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Edit Product</h1>\r\n\t<form class="form-horizontal" method="POST">\r\n')
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
        __M_writer('\t\t<br/><button class="btn btn-primary" type="submit">Submit</button>\r\n\t\t<a class="btn btn-danger" href="/homepage/products/">Cancel</a>\r\n\t</form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Derek\\Documents\\GitHub\\CHF\\test_dmp\\homepage\\templates/products.edit.html", "line_map": {"35": 1, "69": 63, "45": 3, "27": 0, "52": 3, "53": 6, "54": 7, "55": 8, "56": 8, "57": 8, "58": 8, "59": 10, "60": 10, "61": 11, "62": 11, "63": 15}, "uri": "products.edit.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
