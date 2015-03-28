# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427300981.048848
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/products.html'
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
        request = context.get('request', UNDEFINED)
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
        request = context.get('request', UNDEFINED)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Products</h1>\r\n\t<table class="table table-striped table-bordered">\r\n\t\t<tr>\r\n\t\t\t<th>Name</th>\r\n\t\t\t<th>Quantity on Hand</th>\r\n\t\t\t<th>Shelf Location</th>\r\n\t\t\t<th>Order File</th>\r\n\t\t\t<th>Description</th>\r\n\t\t\t<th>Manufacturer</th>\r\n\t\t\t<th>Price</th>\r\n\t\t\t<th>SKU</th>\r\n\t\t\t<th>Order Form Name</th>\r\n\t\t\t<th>Production Time</th>\r\n\t\t\t<th>Vendor</th>\r\n\t\t\t<th>Category</th>\r\n')
        if request.user.has_perm('homepage.is_manager'):
            __M_writer('\t\t\t\t<th>Actions</th>\r\n')
        __M_writer('\t\t</tr>\r\n')
        for product in products:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(product.name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.quantity_on_hand))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.shelf_location))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.order_file))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.description))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.manufacturer))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.average_cost))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.sku))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.order_form_name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.production_time))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.vendor))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.category))
            __M_writer('</td>\r\n')
            if request.user.has_perm('homepage.is_manager'):
                __M_writer('\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<a href="/homepage/products.edit/')
                __M_writer(str(product.id))
                __M_writer('/">Edit </a>\r\n\t\t\t\t\t\t|\r\n\t\t\t\t\t\t<a href="/homepage/products.delete/')
                __M_writer(str(product.id))
                __M_writer('/">Delete</a>\r\n\t\t\t\t\t</td>\r\n')
            __M_writer('\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n')
        if request.user.has_perm('homepage.is_manager'):
            __M_writer('\t\t<div class="text-right">\r\n\t\t\t<a class="btn btn-primary" href="/homepage/products.create/">Add Product</a>\r\n\t\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"27": 0, "36": 1, "46": 3, "54": 3, "55": 19, "56": 20, "57": 22, "58": 23, "59": 24, "60": 25, "61": 25, "62": 26, "63": 26, "64": 27, "65": 27, "66": 28, "67": 28, "68": 29, "69": 29, "70": 30, "71": 30, "72": 31, "73": 31, "74": 32, "75": 32, "76": 33, "77": 33, "78": 34, "79": 34, "80": 35, "81": 35, "82": 36, "83": 36, "84": 37, "85": 38, "86": 39, "87": 39, "88": 41, "89": 41, "90": 44, "91": 46, "92": 47, "93": 48, "99": 93}, "uri": "products.html", "filename": "C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/products.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
