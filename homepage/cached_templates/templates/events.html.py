# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423370116.203491
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/events.html'
_template_uri = 'events.html'
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
        events = context.get('events', UNDEFINED)
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
        events = context.get('events', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>Events</h1>\r\n\t<table class="table table-striped table-bordered">\r\n\t\t<tr>\r\n\t\t\t<th>ID</th>\r\n\t\t\t<th>Name</th>\r\n\t\t\t<th>Start Date</th>\r\n\t\t\t<th>End Date</th>\r\n')
        if request.user.has_perm('homepage.is_manager'):
            __M_writer('\t\t\t\t<th>Actions</th\r\n')
        __M_writer('\t\t</tr>\r\n')
        for event in events:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(event.id))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(event.name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(event.start_date))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(event.end_date))
            __M_writer('</td>\r\n')
            if request.user.has_perm('homepage.is_manager'):
                __M_writer('\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<a href="/homepage/events.edit/')
                __M_writer(str(event.id))
                __M_writer('/">Edit </a>\r\n\t\t\t\t\t\t| \r\n\t\t\t\t\t\t<a href="/homepage/events.delete/')
                __M_writer(str(event.id))
                __M_writer('/">Delete</a>\r\n\t\t\t\t\t</td>\r\n')
            __M_writer('\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n')
        if request.user.has_perm('homepage.is_manager'):
            __M_writer('\t\t<div class="text-right">\r\n\t\t\t<a class="btn btn-primary" href="/homepage/events.create/">Add New Event</a>\r\n\t\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "events.html", "filename": "C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/events.html", "source_encoding": "ascii", "line_map": {"64": 19, "65": 19, "66": 20, "67": 20, "68": 21, "69": 22, "70": 23, "71": 23, "72": 25, "73": 25, "74": 28, "75": 30, "76": 31, "77": 32, "83": 77, "27": 0, "36": 1, "46": 3, "54": 3, "55": 11, "56": 12, "57": 14, "58": 15, "59": 16, "60": 17, "61": 17, "62": 18, "63": 18}}
__M_END_METADATA
"""
