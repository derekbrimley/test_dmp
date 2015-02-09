# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423503961.113612
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\Documents\\GitHub\\CHF\\test_dmp\\homepage\\templates/orders.html'
_template_uri = 'orders.html'
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
        orders = context.get('orders', UNDEFINED)
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
        orders = context.get('orders', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Orders</h1>\r\n\t<table class="table table-striped table-bordered">\r\n\t\t<tr>\r\n\t\t\t<th>ID</th>\r\n\t\t\t<th>Order Date</th>\r\n\t\t\t<th>Date Packed</th>\r\n\t\t\t<th>Date Paid</th>\r\n\t\t\t<th>Date Shipped</th>\r\n\t\t\t<th>Tracking Number</th>\r\n')
        if request.user.has_perm('homepage.is_manager'):
            __M_writer('\t\t\t\t<th>Actions</th>\r\n')
        __M_writer('\t\t</tr>\r\n')
        for order in orders:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(order.id))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(order.order_date))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(order.date_packed))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(order.date_paid))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(order.date_shipped))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(order.tracking_number))
            __M_writer('</td>\r\n')
            if request.user.has_perm('homepage.is_manager'):
                __M_writer('\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<a href="/homepage/orders.edit/')
                __M_writer(str(order.id))
                __M_writer('/">Edit </a>\r\n\t\t\t\t\t\t| \r\n\t\t\t\t\t\t<a href="/homepage/orders.delete/')
                __M_writer(str(order.id))
                __M_writer('/">Delete</a>\r\n\t\t\t\t\t</td>\r\n')
            __M_writer('\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\t<div class="text-right">\r\n\t\t<a class="btn btn-primary" href="/homepage/orders.create/">Create New Order</a>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Derek\\Documents\\GitHub\\CHF\\test_dmp\\homepage\\templates/orders.html", "line_map": {"64": 21, "65": 21, "66": 22, "67": 22, "68": 23, "69": 23, "70": 24, "71": 24, "72": 25, "73": 26, "74": 27, "75": 27, "76": 29, "77": 29, "78": 32, "79": 34, "85": 79, "27": 0, "36": 1, "46": 3, "54": 3, "55": 13, "56": 14, "57": 16, "58": 17, "59": 18, "60": 19, "61": 19, "62": 20, "63": 20}, "uri": "orders.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
