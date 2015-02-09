# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423370360.068422
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
        items = context.get('items', UNDEFINED)
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
        items = context.get('items', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Items</h1>\r\n\t<table class="table table-striped table-bordered">\r\n\t\t<tr>\r\n\t\t\t<th>ID</th>\r\n\t\t\t<th>Name</th>\r\n\t\t\t<th>Description</th>\r\n\t\t\t<th>Value</th>\r\n\t\t\t<th>Rental Price</th>\r\n\t\t\t<th>Rentable</th>\r\n\t\t\t<th>Actions</th>\r\n\t\t<tr>\r\n')
        for item in items:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(item.id))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.description))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.value))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.standard_rental_price))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(item.rentable))
            __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/homepage/items.edit/')
            __M_writer(str(item.id))
            __M_writer('/">Edit </a>\r\n\t\t\t\t| \r\n\t\t\t\t<a href="/homepage/items.delete/')
            __M_writer(str(item.id))
            __M_writer('/">Delete</td></a>\r\n\t\t\t<tr>\r\n')
        __M_writer('\t</table>\r\n\t<div class="text-right">\r\n\t\t<a class="btn btn-primary" href="/homepage/items.create/">Add Item</a>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "items.html", "filename": "C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/items.html", "source_encoding": "ascii", "line_map": {"64": 21, "65": 22, "66": 22, "67": 24, "68": 24, "69": 26, "70": 26, "71": 29, "77": 71, "27": 0, "35": 1, "45": 3, "52": 3, "53": 15, "54": 16, "55": 17, "56": 17, "57": 18, "58": 18, "59": 19, "60": 19, "61": 20, "62": 20, "63": 21}}
__M_END_METADATA
"""
