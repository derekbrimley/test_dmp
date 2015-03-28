# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427508405.232978
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.html'
_template_uri = 'products.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t\r\n')
        for product in products:
            __M_writer('\t\t<div class="product_container">\r\n\t\t\t<img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('catalog/media/')
            __M_writer(str( product.id ))
            __M_writer('.jpg"/>\r\n\t\t\t<div data-id="')
            __M_writer(str( product.id ))
            __M_writer('" class="product_name">\r\n\t\t\t\t')
            __M_writer(str(product.name))
            __M_writer('\r\n\t\t\t</div>\r\n\t\t\t<div class="text-right">\r\n\t\t\t\t<a href="/catalog/products.detail/')
            __M_writer(str( product.id ))
            __M_writer('/">\r\n\t\t\t\t\t<button class="submit_btn btn btn-warning">View Details</button>\r\n\t\t\t\t</a>\r\n\t\t\t</div>\r\n\t\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 10, "65": 13, "66": 13, "27": 0, "36": 1, "72": 66, "46": 3, "54": 3, "55": 6, "56": 7, "57": 8, "58": 8, "59": 8, "60": 8, "61": 9, "62": 9, "63": 10}, "filename": "C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.html", "uri": "products.html"}
__M_END_METADATA
"""
