# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425626436.129507
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        product_info = context.get('product_info', UNDEFINED)
        products = context.get('products', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        product_info = context.get('product_info', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        for product in products:
            __M_writer('\t\t<div class="product_container">\r\n')
            for product in products:
                if product_info.id == product.product_specification_id:
                    __M_writer('\t\t\t\t\t<img src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('catalog/media/')
                    __M_writer(str( product.id ))
                    __M_writer('.jpg"/>\r\n\t\t\t\t\t<div class="product_name">\r\n\t\t\t\t\t\t')
                    __M_writer(str(product.name))
                    __M_writer('\r\n\t\t\t\t\t</div>\r\n')
            __M_writer('\t\t\t<div class="text-right">\r\n\t\t\t\t<button id="submit_btn" class="btn btn-warning">Add to Cart</button>\r\n\t\t\t</div>\r\n\t\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 9, "65": 9, "66": 11, "27": 0, "68": 15, "37": 1, "74": 68, "47": 3, "67": 11, "56": 3, "57": 5, "58": 6, "59": 7, "60": 8, "61": 9, "62": 9, "63": 9}, "uri": "search.results.html", "filename": "C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/search.results.html"}
__M_END_METADATA
"""
