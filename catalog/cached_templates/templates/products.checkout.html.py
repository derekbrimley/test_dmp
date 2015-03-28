# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427507892.5589
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
        __M_writer('\r\n\t<h1>Checkout</h1>\r\n\t<h2>Items currently in your cart:</h2><br/>\r\n\t<div class="shopping_cart">\r\n\t\t<table class="table table-striped table-bordered">\r\n\t\t\t<tr>\r\n\t\t\t\t<th class="table_header"></th>\r\n\t\t\t\t<th class="table_header">Product</th>\r\n\t\t\t\t<th class="table_header">Quantity</th>\r\n\t\t\t\t<th class="table_header">Total Price</th>\r\n\t\t\t\t<th></th>\r\n\t\t\t</tr>\r\n')
        for item in items:
            __M_writer('\t\t\t\t<tr>\r\n\t\t\t\t\t<td class="picture">\r\n\t\t\t\t\t\t<img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('catalog/media/')
            __M_writer(str( item.id ))
            __M_writer('.jpg"/>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td class="name">\r\n\t\t\t\t\t\t<div data-id="')
            __M_writer(str( item.id ))
            __M_writer('" class="product_name">\r\n\t\t\t\t\t\t\t')
            __M_writer(str(item.name))
            __M_writer('\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t\t<td class="quantity">')
            __M_writer(str( shopping_cart[ str(item.id) ]))
            __M_writer('<br></td>\r\n\t\t\t\t\t<td class="total_price">$')
            __M_writer(str(int(item.price) * int(shopping_cart[ str(item.id) ])))
            __M_writer('</td>\r\n\t\t\t\t\t<td class="delete">\r\n\t\t\t\t\t\t<span class="btn btn-primary">\r\n\t\t\t\t\t\t\t<a href="/catalog/products.detail/')
            __M_writer(str(item.id))
            __M_writer('/" class="text-right" ><p>Info</p></a>\r\n\t\t\t\t\t\t</span>\r\n\t\t\t\t\t\t<button id="delete_btn" class="btn btn-danger">\r\n\t\t\t\t\t\t\t<p data-id="')
            __M_writer(str( item.id ))
            __M_writer('" class="delete_btn">Delete</p>\r\n\t\t\t\t\t\t</button>\r\n\t\t\t\t\t</td>\r\n\t\t\t\t</tr>\r\n')
        __M_writer('\t\t</table><br>\r\n\t\t<div class="check_out">\r\n\t\t\t<button id="check_out_btn" class="btn btn-warning">Complete Purchase</button>\r\n\t\t</div>\r\n\t\t<div class="shopping_cart_info">\r\n\t\t\t<p>Total Cost: $')
        __M_writer(str( total_price ))
        __M_writer('</p>\r\n\t\t</div>\r\n\t\t<div class="back_shopping">\r\n\t\t\t<a href="/catalog/products/">\r\n\t\t\t\t<button id="check_out_btn" class="btn btn-success">Keep Shopping</button>\r\n\t\t\t</a><br><br>\r\n\t\t</div>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 16, "65": 18, "66": 18, "67": 18, "68": 18, "69": 21, "70": 21, "71": 22, "72": 22, "73": 25, "74": 25, "75": 26, "76": 26, "77": 29, "78": 29, "79": 32, "80": 32, "81": 37, "82": 42, "83": 42, "89": 83, "27": 0, "40": 1, "50": 3, "62": 3, "63": 15}, "filename": "C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.checkout.html", "uri": "products.checkout.html"}
__M_END_METADATA
"""
