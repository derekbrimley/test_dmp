# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427313768.549975
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/batch_processes.html'
_template_uri = 'batch_processes.html'
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
        overdue_items_info = context.get('overdue_items_info', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        overdue_items = context.get('overdue_items', UNDEFINED)
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
        overdue_items_info = context.get('overdue_items_info', UNDEFINED)
        def content():
            return render_content(context)
        overdue_items = context.get('overdue_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Overdue Rentals</h1><br/>\r\n\t<table class="table table-striped">\r\n\t\t<tr>\r\n\t\t\t<th>Product ID:</th>\r\n\t\t\t<th>Product Name:</th>\r\n\t\t\t<th>Renter:</th>\r\n\t\t\t<th>Due Date:</th>\r\n\t\t</tr>\r\n')
        for overdue_item in overdue_items: ##gets all overdue items
            for overdue_item_info in overdue_items_info:
                if overdue_item.rentable_product_id == overdue_item_info.id:
                    __M_writer('\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<td>')
                    __M_writer(str(overdue_item_info.id))
                    __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                    __M_writer(str(overdue_item_info.name))
                    __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                    __M_writer(str(overdue_item_info.order_form_name))
                    __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                    __M_writer(str(overdue_item.date_due))
                    __M_writer('</td>\r\n\t\t\t\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/batch_processes.html", "source_encoding": "ascii", "line_map": {"64": 18, "65": 19, "66": 19, "27": 0, "36": 1, "73": 67, "46": 3, "67": 24, "54": 3, "55": 12, "56": 13, "57": 14, "58": 15, "59": 16, "60": 16, "61": 17, "62": 17, "63": 18}, "uri": "batch_processes.html"}
__M_END_METADATA
"""
