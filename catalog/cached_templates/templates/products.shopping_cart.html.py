# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425796648.466651
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.shopping_cart.html'
_template_uri = 'products.shopping_cart.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        str = context.get('str', UNDEFINED)
        product_info = context.get('product_info', UNDEFINED)
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        shopping_cart = context.get('shopping_cart', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        str = context.get('str', UNDEFINED)
        product_info = context.get('product_info', UNDEFINED)
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context)
        shopping_cart = context.get('shopping_cart', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        for item in items:
            __M_writer('\t\t<div id="product_container">\r\n')
            for info in product_info:
                if info.id == item.product_specification_id:
                    __M_writer('\t\t\t\t\t<img src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('catalog/media/')
                    __M_writer(str( info.id ))
                    __M_writer('.jpg"/>\r\n\t\t\t\t\t<div data-id="')
                    __M_writer(str( item.id ))
                    __M_writer('" class="product_name">\r\n\t\t\t\t\t\t')
                    __M_writer(str(info.name))
                    __M_writer('\r\n\t\t\t\t\t</div>\r\n')
            __M_writer('\t\t\tQuantity: ')
            __M_writer(str( shopping_cart[ str(item.id) ]))
            __M_writer('\r\n\t\t\t<span class="btn btn-danger">\r\n\t\t\t\t<p data-id="')
            __M_writer(str( item.id ))
            __M_writer('" class="delete_btn" >Delete</p>\r\n\t\t\t</span>\r\n\t\t</div>\r\n')
        __M_writer('\t<span class="text-right">\r\n\t\t<a href="/catalog/products.checkout/">\r\n\t\t\t<button id="check_out_btn" class="btn btn-warning">Check Out</button>\r\n\t\t</a>\r\n\t</span>\r\n\t<span class="text-right">\r\n\t\t<a href="/catalog/products/">\r\n\t\t\t<button id="check_out_btn" class="btn btn-success">Close</button>\r\n\t\t</a>\r\n\t</span>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 6, "65": 7, "66": 8, "67": 8, "68": 8, "69": 8, "70": 8, "71": 9, "72": 9, "73": 10, "74": 10, "75": 14, "76": 14, "77": 14, "78": 16, "79": 16, "80": 20, "86": 80, "27": 0, "39": 1, "44": 30, "50": 3, "61": 3, "62": 4, "63": 5}, "uri": "products.shopping_cart.html", "filename": "C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.shopping_cart.html"}
__M_END_METADATA
"""
