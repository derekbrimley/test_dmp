# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427261212.732768
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.detail.html'
_template_uri = 'products.detail.html'
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
        product = context.get('product', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="product_container">\r\n\t\t<img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('catalog/media/')
        __M_writer(str( product.id ))
        __M_writer('.jpg"/>\r\n\t\t<div class="product_info">\r\n\t\t\t<span class="product_attribute">Name: </span>')
        __M_writer(str(product.name))
        __M_writer('<br/>\r\n\t\t\t<span class="product_attribute">Description: </span>')
        __M_writer(str(product.description))
        __M_writer(' <br/>\r\n\t\t\t<span class="product_attribute">Price: </span>')
        __M_writer(str(product.price))
        __M_writer('\r\n\t\t</div>\r\n\t\t<div class="text-right">\r\n\t\t\tQuantity: \r\n\t\t\t<select id="quantity">\r\n\t\t\t  <option value="1">1</option>\r\n\t\t\t  <option value="2">2</option>\r\n\t\t\t  <option value="3">3</option>\r\n\t\t\t  <option value="4">4</option>\r\n\t\t\t  <option value="5">5</option>\r\n\t\t\t</select>\r\n\t\t\t<button id="add_btn" class="btn btn-warning" data-id="')
        __M_writer(str(product.id))
        __M_writer('">Add to Cart</button>\r\n\t\t</div>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 9, "65": 20, "66": 20, "27": 0, "36": 1, "72": 66, "46": 3, "54": 3, "55": 5, "56": 5, "57": 5, "58": 5, "59": 7, "60": 7, "61": 8, "62": 8, "63": 9}, "uri": "products.detail.html", "filename": "C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.detail.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
