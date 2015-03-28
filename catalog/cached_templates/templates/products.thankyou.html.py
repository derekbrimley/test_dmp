# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427510017.577303
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.thankyou.html'
_template_uri = 'products.thankyou.html'
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
        billing_info = context.get('billing_info', UNDEFINED)
        int = context.get('int', UNDEFINED)
        items = context.get('items', UNDEFINED)
        total_price = context.get('total_price', UNDEFINED)
        shopping_cart = context.get('shopping_cart', UNDEFINED)
        str = context.get('str', UNDEFINED)
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
        billing_info = context.get('billing_info', UNDEFINED)
        int = context.get('int', UNDEFINED)
        items = context.get('items', UNDEFINED)
        total_price = context.get('total_price', UNDEFINED)
        shopping_cart = context.get('shopping_cart', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Thank you for your purchase!</h1>\r\n\t<h2>Items Purchased:</h2>\r\n')
        for item in items:
            __M_writer('\t\t<p>Item: ')
            __M_writer(str(item.name))
            __M_writer('</p>\r\n\t\t<p>Quantity: ')
            __M_writer(str( shopping_cart[ str(item.id) ]))
            __M_writer('</p>\r\n\t\t<p>Price: ')
            __M_writer(str(int(item.price) * int(shopping_cart[ str(item.id) ])))
            __M_writer('</p>\r\n')
        __M_writer('\t<h2>Shipping Address:</h2>\r\n\t<p>Street: ')
        __M_writer(str(billing_info[0]))
        __M_writer('</p>\r\n\t<p>City: ')
        __M_writer(str(billing_info[1]))
        __M_writer('</p>\r\n\t<p>State: ')
        __M_writer(str(billing_info[2]))
        __M_writer('</p>\r\n\t<p>Zip Code: ')
        __M_writer(str(billing_info[3]))
        __M_writer('</p>\r\n\t<h2>Billing Info:</h2>\r\n\t<p>Card Number: ')
        __M_writer(str(billing_info[4]))
        __M_writer('</p>\r\n\t<p>Expiration: ')
        __M_writer(str(billing_info[5]))
        __M_writer('</p>\r\n\t<p>CVC Number: ***</p>\r\n\t<p>Total Cost: $ ')
        __M_writer(str( total_price ))
        __M_writer('.00</p>\r\n\t\r\n\t<a id="close_btn" class="btn btn-success">Close</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.thankyou.html", "line_map": {"64": 7, "65": 7, "66": 7, "67": 8, "68": 8, "69": 9, "70": 9, "71": 11, "72": 12, "73": 12, "74": 13, "75": 13, "76": 14, "77": 14, "78": 15, "79": 15, "80": 17, "81": 17, "82": 18, "83": 18, "84": 20, "85": 20, "27": 0, "91": 85, "40": 1, "50": 3, "62": 3, "63": 6}, "source_encoding": "ascii", "uri": "products.thankyou.html"}
__M_END_METADATA
"""
