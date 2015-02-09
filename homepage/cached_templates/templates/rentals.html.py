# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423370934.328334
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/rentals.html'
_template_uri = 'rentals.html'
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
        rentals = context.get('rentals', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
        rentals = context.get('rentals', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Rentals</h1>\r\n\t<table class="table table-striped table-bordered">\r\n\t\t<tr>\r\n\t\t\t<th>ID</th>\r\n\t\t\t<th>Rental Time</th>\r\n\t\t\t<th>Due Date</th>\r\n\t\t\t<th>Discount Percent</th>\r\n')
        if request.user.has_perm('homepage.is_manager'):
            __M_writer('\t\t\t\t<th>Actions</th>\r\n')
        __M_writer('\t\t</tr>\r\n')
        for rental in rentals:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(rental.id))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(rental.rental_time))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(rental.due_date))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(rental.discount_percent))
            __M_writer('</td>\r\n')
            if request.user.has_perm('homepage.is_manager'):
                __M_writer('\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<a href="/homepage/rentals.edit/')
                __M_writer(str(rental.id))
                __M_writer('/">Edit </a>\r\n\t\t\t\t\t\t| \r\n\t\t\t\t\t\t<a href="/homepage/rentals.delete/')
                __M_writer(str(rental.id))
                __M_writer('/">Delete</a>\r\n\t\t\t\t\t</td>\r\n')
            __M_writer('\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n\t<div class="text-right">\r\n\t\t<a class="btn btn-primary" href="/homepage/rentals.create/">Create New Rental</a>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/rentals.html", "uri": "rentals.html", "line_map": {"64": 19, "65": 19, "66": 20, "67": 20, "68": 21, "69": 22, "70": 23, "71": 23, "72": 25, "73": 25, "74": 28, "75": 30, "81": 75, "27": 0, "36": 1, "46": 3, "54": 3, "55": 11, "56": 12, "57": 14, "58": 15, "59": 16, "60": 17, "61": 17, "62": 18, "63": 18}}
__M_END_METADATA
"""
