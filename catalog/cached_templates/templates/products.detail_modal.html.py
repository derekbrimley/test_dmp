# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425762762.9164
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.detail_modal.html'
_template_uri = 'products.detail_modal.html'
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
        product = context.get('product', UNDEFINED)
        product_info = context.get('product_info', UNDEFINED)
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
        product = context.get('product', UNDEFINED)
        product_info = context.get('product_info', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="product_container">\r\n')
        if product.id == product.product_specification_id:
            __M_writer('\t\t\t<img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('catalog/media/')
            __M_writer(str( product.id ))
            __M_writer('.jpg"/>\r\n\t\t\t<div class="product_info">\r\n\t\t\t\t<span class="product_attribute">Name: </span>')
            __M_writer(str(product_info.name))
            __M_writer('<br/>\r\n\t\t\t\t<span class="product_attribute">Description: </span>')
            __M_writer(str(product_info.description))
            __M_writer(' <br/>\r\n\t\t\t\t<span class="product_attribute">Price: </span>')
            __M_writer(str(product_info.price))
            __M_writer('\r\n\t\t\t</div>\r\n')
        __M_writer('\t\t<div class="text-right">\r\n\t\t\t<button id="add_btn" class="btn btn-warning">Add to Cart</button>\r\n\t\t</div>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.detail_modal.html", "line_map": {"64": 8, "65": 9, "66": 9, "27": 0, "68": 10, "37": 1, "75": 69, "47": 3, "67": 10, "69": 13, "56": 3, "57": 5, "58": 6, "59": 6, "60": 6, "61": 6, "62": 6, "63": 8}, "uri": "products.detail_modal.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
