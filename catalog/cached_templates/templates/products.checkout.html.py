# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425796971.177268
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
        __M_writer('\r\n\t<h1>Checkout</h1>\r\n\t<h2>Items currently in your cart:</h2><br/>\r\n\t<div class="shopping_cart">\r\n')
        for item in items:
            __M_writer('\t\t\t<div id="product_container">\r\n')
            for info in product_info:
                if info.id == item.product_specification_id:
                    __M_writer('\t\t\t\t\t\t<img src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('catalog/media/')
                    __M_writer(str( info.id ))
                    __M_writer('.jpg"/>\r\n\t\t\t\t\t\t<div data-id="')
                    __M_writer(str( item.id ))
                    __M_writer('" class="product_name">\r\n\t\t\t\t\t\t\t')
                    __M_writer(str(info.name))
                    __M_writer('\r\n\t\t\t\t\t\t</div>\r\n')
            __M_writer('\t\t\t\tQuantity: ')
            __M_writer(str( shopping_cart[ str(item.id) ]))
            __M_writer('\r\n\t\t\t\t<span class="btn btn-danger">\r\n\t\t\t\t\t<p data-id="')
            __M_writer(str( item.id ))
            __M_writer('" class="delete_btn" >Delete</p>\r\n\t\t\t\t</span>\r\n\t\t\t</div>\r\n')
        __M_writer('\t</div>\r\n\t<span class="text-right">\r\n\t\t<button id="check_out_btn" class="btn btn-warning">Complete Purchase</button>\r\n\t</span>\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 10, "65": 11, "66": 11, "67": 11, "68": 11, "69": 11, "70": 12, "71": 12, "72": 13, "73": 13, "74": 17, "75": 17, "76": 17, "77": 19, "78": 19, "79": 23, "85": 79, "27": 0, "39": 1, "49": 3, "60": 3, "61": 7, "62": 8, "63": 9}, "uri": "products.checkout.html", "filename": "C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.checkout.html"}
__M_END_METADATA
"""
