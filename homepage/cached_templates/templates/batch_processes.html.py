# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425795809.186703
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
        product_specifications = context.get('product_specifications', UNDEFINED)
        overdue_items = context.get('overdue_items', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        rental_items = context.get('rental_items', UNDEFINED)
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
        product_specifications = context.get('product_specifications', UNDEFINED)
        overdue_items = context.get('overdue_items', UNDEFINED)
        def content():
            return render_content(context)
        rental_items = context.get('rental_items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Overdue Rentals</h1><br/>\r\n\t<table class="table table-striped">\r\n\t\t<tr>\r\n\t\t\t<th>Product ID:</th>\r\n\t\t\t<th>Product Name:</th>\r\n\t\t\t<th>Renter:</th>\r\n\t\t\t<th>Due Date:</th>\r\n\t\t</tr>\r\n')
        for rental_item in rental_items: ##gets all items
            for overdue_item in overdue_items: ##gets all overdue items
                if overdue_item == rental_item.id: ##gets all data for items that are overdue
                    for product_specification in product_specifications:  ##finds the product information in the product_specification table
                        if product_specification.id == rental_item.rentable_product_id:  ##matches up overdue items to product_specification
                            __M_writer('\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<td>')
                            __M_writer(str(product_specification.id))
                            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
                            __M_writer(str(product_specification.name))
                            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
                            __M_writer(str(product_specification.order_form_name))
                            __M_writer('</td>\r\n\t\t\t\t\t\t<td>')
                            __M_writer(str(rental_item.date_due))
                            __M_writer('</td>\r\n\r\n\t\t\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 18, "65": 19, "66": 19, "27": 0, "68": 20, "37": 1, "70": 21, "71": 29, "77": 71, "47": 3, "67": 20, "69": 21, "56": 3, "57": 12, "58": 13, "59": 14, "60": 15, "61": 16, "62": 17, "63": 18}, "uri": "batch_processes.html", "filename": "C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/batch_processes.html"}
__M_END_METADATA
"""
