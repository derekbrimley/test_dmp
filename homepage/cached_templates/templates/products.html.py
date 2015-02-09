# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423370358.67296
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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Products</h1>\r\n\t<table class="table table-striped table-bordered">\r\n\t\t<tr>\r\n\t\t\t<th>ID</th>\r\n\t\t\t<th>Name</th>\r\n\t\t\t<th>Description</th>\r\n\t\t\t<th>Category</th>\r\n\t\t\t<th>Price</th>\r\n')
        if request.user.has_perm('homepage.is_manager'):
            __M_writer('\t\t\t\t<th>Actions</th>\r\n')
        __M_writer('\t\t</tr>\r\n')
        for product in products:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(product.id))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.description))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.category))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(product.current_price))
            __M_writer('</td>\r\n')
            if request.user.has_perm('homepage.is_manager'):
                __M_writer('\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<a href="/homepage/products.edit/')
                __M_writer(str(product.id))
                __M_writer('/">Edit </a>\r\n\t\t\t\t\t\t| \r\n\t\t\t\t\t\t<a href="/homepage/products.delete/')
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
{"uri": "products.html", "filename": "C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/products.html", "source_encoding": "ascii", "line_map": {"64": 20, "65": 20, "66": 21, "67": 21, "68": 22, "69": 22, "70": 23, "71": 24, "72": 25, "73": 25, "74": 27, "75": 27, "76": 30, "77": 32, "78": 33, "79": 34, "85": 79, "27": 0, "36": 1, "46": 3, "54": 3, "55": 12, "56": 13, "57": 15, "58": 16, "59": 17, "60": 18, "61": 18, "62": 19, "63": 19}}
__M_END_METADATA
"""
