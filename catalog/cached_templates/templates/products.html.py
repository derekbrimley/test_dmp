# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425788185.466781
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
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products_info = context.get('products_info', UNDEFINED)
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
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products_info = context.get('products_info', UNDEFINED)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\tSearch: \r\n\t<form id=#"search_box">\r\n\t\t<input id="search_box"></input><br/>\r\n\t</form>\r\n')
        for product in products:
            __M_writer('\t\t<div class="product_container">\r\n')
            for product_info in products_info:
                if product_info.id == product.product_specification_id:
                    __M_writer('\t\t\t\t\t<img src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('catalog/media/')
                    __M_writer(str( product_info.id ))
                    __M_writer('.jpg"/>\r\n\t\t\t\t\t<div data-id="')
                    __M_writer(str( product.id ))
                    __M_writer('" class="product_name">\r\n\t\t\t\t\t\t')
                    __M_writer(str(product_info.name))
                    __M_writer('\r\n\t\t\t\t\t</div>\r\n')
            __M_writer('\t\t\t<div class="text-right">\r\n\t\t\t\t<a href="/catalog/products.detail/')
            __M_writer(str( product.id ))
            __M_writer('/">\r\n\t\t\t\t\t<button class="submit_btn btn btn-warning">View Details</button>\r\n\t\t\t\t</a>\r\n\t\t\t</div>\r\n\t\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 13, "65": 13, "66": 14, "27": 0, "68": 15, "37": 1, "70": 19, "71": 20, "72": 20, "78": 72, "47": 3, "67": 14, "69": 15, "56": 3, "57": 9, "58": 10, "59": 11, "60": 12, "61": 13, "62": 13, "63": 13}, "source_encoding": "ascii", "filename": "C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.html", "uri": "products.html"}
__M_END_METADATA
"""
