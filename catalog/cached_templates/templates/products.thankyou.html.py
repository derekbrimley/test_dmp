# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425793171.292849
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
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Thank you for your purchase!</h1>\r\n\t<h2>Shipping Address:</h2>\r\n\t<p>Street: ')
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
        __M_writer('</p>\r\n\t<p>CVC Number: ***</p>\r\n\t\r\n\t<a class="btn btn-success" href="/catalog/products.shopping_cart/">Close</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "products.thankyou.html", "filename": "C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/products.thankyou.html", "line_map": {"64": 12, "35": 1, "70": 64, "45": 3, "27": 0, "52": 3, "53": 6, "54": 6, "55": 7, "56": 7, "57": 8, "58": 8, "59": 9, "60": 9, "61": 11, "62": 11, "63": 12}}
__M_END_METADATA
"""
