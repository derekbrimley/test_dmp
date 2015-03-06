# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425398340.330137
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/items.html'
_template_uri = 'items.html'
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
        items = context.get('items', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Items</h1>\r\n\t<table class="table table-striped table-bordered">\r\n\t\t<tr>\r\n\t\t\t<th>ID</th>\r\n\t\t\t<th>Quantity on Hand</th>\r\n\t\t\t<th>Replacement Price</th>\r\n\t\t\t<th>Shelf Location</th>\r\n\t\t\t<th>Order File</th>\r\n\t\t\t<th>Serial Number</th>\r\n\t\t\t<th>Date Acquired</th>\r\n\t\t\t<th>Status</th>\r\n\t\t\t<th>For Sale</th>\r\n\t\t\t<th>Rentable</th>\r\n\t\t\t<th>Notes</th>\r\n\t\t\t<th>Times Rented</th>\r\n\t\t\t<th>Price Per Day</th>\r\n\t\t\t<th>Replacement Price</th>\r\n')
        if request.user.has_perm('homepage.is_manager'):
            __M_writer('\t\t\t\t<th>Actions</th>\r\n')
        __M_writer('\t\t</tr>\r\n')
        for item in items:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(item.id))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.quantity_on_hand))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.shelf_location))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.order_file))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.serial_number))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.date_acquired))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.cost))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.status))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.for_sale))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.is_rentable))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.notes))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.times_rented))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.price_per_day))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.replacement_price))
            __M_writer('</td>\r\n')
            if request.user.has_perm('homepage.is_manager'):
                __M_writer('\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<a href="/homepage/items.edit/')
                __M_writer(str(item.id))
                __M_writer('/">Edit </a>\r\n\t\t\t\t\t\t|\r\n\t\t\t\t\t\t<a href="/homepage/items.delete/')
                __M_writer(str(item.id))
                __M_writer('/">Delete</a>\r\n\t\t\t\t\t</td>\r\n')
            __M_writer('\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n')
        if request.user.has_perm('homepage.is_manager'):
            __M_writer('\t\t<div class="text-right">\r\n\t\t\t<a class="btn btn-primary" href="/homepage/items.create/">Add Product</a>\r\n\t\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"27": 0, "36": 1, "46": 3, "54": 3, "55": 21, "56": 22, "57": 24, "58": 25, "59": 26, "60": 27, "61": 27, "62": 28, "63": 28, "64": 29, "65": 29, "66": 30, "67": 30, "68": 31, "69": 31, "70": 32, "71": 32, "72": 33, "73": 33, "74": 34, "75": 34, "76": 35, "77": 35, "78": 36, "79": 36, "80": 37, "81": 37, "82": 38, "83": 38, "84": 39, "85": 39, "86": 40, "87": 40, "88": 41, "89": 42, "90": 43, "91": 43, "92": 45, "93": 45, "94": 48, "95": 50, "96": 51, "97": 52, "103": 97}, "uri": "items.html", "filename": "C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/items.html"}
__M_END_METADATA
"""
