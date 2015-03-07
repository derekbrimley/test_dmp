# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425674149.694827
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/search.results.html'
_template_uri = 'search.results.html'
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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        product = context.get('product', UNDEFINED)
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
        product = context.get('product', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if product is UNDEFINED:
            __M_writer('\t\t<div class="product_container">\r\n\t\t\r\n\t\t\t')
            __M_writer(str( product ))
            __M_writer('\r\n\t\t\r\n\t\t</div>\r\n')
        else:
            __M_writer('\t\t<div>\r\n\t\t\tProduct not found.\r\n\t\t</div>\r\n')
        __M_writer('\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 59, "35": 1, "45": 3, "27": 0, "52": 3, "53": 4, "54": 5, "55": 7, "56": 7, "57": 10, "58": 11, "59": 15}, "uri": "search.results.html", "filename": "C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/search.results.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
