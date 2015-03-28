# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427504101.146969
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.checkout.html'
_template_uri = 'products.checkout.html'
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
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        int = context.get('int', UNDEFINED)
        shopping_cart = context.get('shopping_cart', UNDEFINED)
        total_price = context.get('total_price', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def content():
            return render_content(context)
        int = context.get('int', UNDEFINED)
        shopping_cart = context.get('shopping_cart', UNDEFINED)
        total_price = context.get('total_price', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Checkout</h1>\r\n\t<h2>Items currently in your cart:</h2><br/>\r\n\t<div class="shopping_cart">\r\n')
        for item in items:
            __M_writer('\t\t\t<div id="product_container">\r\n\t\t\t\t<img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('catalog/media/')
            __M_writer(str( item.id ))
            __M_writer('.jpg"/>\r\n\t\t\t\t<div data-id="')
            __M_writer(str( item.id ))
            __M_writer('" class="product_name">\r\n\t\t\t\t\t')
            __M_writer(str(item.name))
            __M_writer('\r\n\t\t\t\t</div>\r\n\t\t\t\tQuantity: ')
            __M_writer(str( shopping_cart[ str(item.id) ]))
            __M_writer('<br>\r\n\t\t\t\tPrice: ')
            __M_writer(str(item.price))
            __M_writer('\r\n\t\t\t\tTotal: ')
            __M_writer(str(int(item.price) * shopping_cart[ str(item.id) ]))
            __M_writer('\r\n\t\t\t\t<span class="btn btn-danger">\r\n\t\t\t\t\t<p data-id="')
            __M_writer(str( item.id ))
            __M_writer('" class="delete_btn" >Delete</p>\r\n\t\t\t\t</span>\r\n\t\t\t</div>\r\n')
        __M_writer('\t</div>\r\n\t<div class="shopping_cart_info">\r\n\t\tTotal Cost: ')
        __M_writer(str( total_price ))
        __M_writer('\r\n\t</div>\r\n\t<span class="text-right">\r\n\t\t<button id="check_out_btn" class="btn btn-warning">Complete Purchase</button>\r\n\t</span>\r\n\t<span class="text-right">\r\n\t\t<a href="/catalog/products/">\r\n\t\t\t<button id="check_out_btn" class="btn btn-success">Keep Shopping</button>\r\n\t\t</a>\r\n\t</span>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 8, "65": 9, "66": 9, "67": 9, "68": 9, "69": 10, "70": 10, "71": 11, "72": 11, "73": 13, "74": 13, "75": 14, "76": 14, "77": 15, "78": 15, "79": 17, "80": 17, "81": 21, "82": 23, "83": 23, "89": 83, "27": 0, "40": 1, "50": 3, "62": 3, "63": 7}, "filename": "C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.checkout.html", "uri": "products.checkout.html"}
__M_END_METADATA
"""
