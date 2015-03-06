# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425405281.692362
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/transactions.html'
_template_uri = 'transactions.html'
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
        transactions = context.get('transactions', UNDEFINED)
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
        transactions = context.get('transactions', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Transactions</h1>\r\n\t<table class="table table-striped table-bordered">\r\n\t\t<tr>\r\n\t\t\t<th>ID</th>\r\n\t\t\t<th>Date</th>\r\n\t\t\t<th>Customer</th>\r\n\t\t\t<th>Date Packed</th>\r\n\t\t\t<th>Packed By</th>\r\n\t\t\t<th>Date Paid</th>\r\n\t\t\t<th>Payment Handler</th>\r\n\t\t\t<th>Date Shipped</th>\r\n\t\t\t<th>Shipped By</th>\r\n\t\t\t<th>Tracking Number</th>\r\n\t\t\t<th>Ships To</th>\r\n\t\t\t<th>Packed By</th>\r\n\t\t\t<th>Payment Processed By</th>\r\n\t\t\t<th>Shipped By</th>\r\n\t\t\t<th>Handled By</th>\r\n')
        if request.user.has_perm('homepage.is_manager'):
            __M_writer('\t\t\t\t<th>Actions</th>\r\n')
        __M_writer('\t\t</tr>\r\n')
        for transaction in transactions:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(transaction.id))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(transaction.date))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(transaction.customer))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(transaction.date_packed))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(transaction.packed_by))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(transaction.date_paid))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(transaction.payment_handler))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(transaction.date_shipped))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(transaction.shipped_by))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(transaction.tracking_number))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(transaction.ships_to))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(transaction.packed_by))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(transaction.payment_processed_by))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(transaction.shipped_by))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(transaction.handled_by))
            __M_writer('</td>\r\n')
            if request.user.has_perm('homepage.is_manager'):
                __M_writer('\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<a href="/homepage/transactions.edit/')
                __M_writer(str(transaction.id))
                __M_writer('/">Edit </a>\r\n\t\t\t\t\t\t| \r\n\t\t\t\t\t\t<a href="/homepage/transactions.delete/')
                __M_writer(str(transaction.id))
                __M_writer('/">Delete</a>\r\n\t\t\t\t\t</td>\r\n')
            __M_writer('\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\t<div class="text-right">\r\n\t\t<a class="btn btn-primary" href="/homepage/transactions.create/">Create New Rental</a>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"27": 0, "36": 1, "46": 3, "54": 3, "55": 22, "56": 23, "57": 25, "58": 26, "59": 27, "60": 28, "61": 28, "62": 29, "63": 29, "64": 30, "65": 30, "66": 31, "67": 31, "68": 32, "69": 32, "70": 33, "71": 33, "72": 34, "73": 34, "74": 35, "75": 35, "76": 36, "77": 36, "78": 37, "79": 37, "80": 38, "81": 38, "82": 39, "83": 39, "84": 40, "85": 40, "86": 41, "87": 41, "88": 42, "89": 42, "90": 43, "91": 44, "92": 45, "93": 45, "94": 47, "95": 47, "96": 50, "97": 52, "103": 97}, "uri": "transactions.html", "filename": "C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/transactions.html"}
__M_END_METADATA
"""
