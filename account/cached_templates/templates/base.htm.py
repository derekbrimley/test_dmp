# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425524501.922328
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\account\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['nav']


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
    return runtime._inherit_from(context, '/base_app/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def nav():
            return render_nav(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav'):
            context['self'].nav(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def nav():
            return render_nav(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="sidebar-nav">\r\n\t\t<ul class="nav nav-pills nav-stacked">\r\n\t\t\t<li role="presentation" class="active">\r\n\t\t\t<a href="/homepage/">\r\n\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-arrow-left" aria-hidden="true"></span> Home\r\n\t\t\t</a>\r\n\t\t\t</li>\r\n\t\t\t<li role="presentation">\r\n\t\t\t\t<a href="/account/create_account/">\r\n\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-plus" aria-hidden="true"></span> Create Account\r\n\t\t\t\t</a>\r\n\t\t\t</li>\r\n\t\t\t<li role="presentation">\r\n\t\t\t\t<a href="/homepage/edit_info/">\r\n\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-pencil" aria-hidden="true"></span> Edit Account\r\n\t\t\t\t</a>\r\n\t\t\t</li>\r\n\t\t\t<li role="presentation">\r\n\t\t\t\t<a href="/homepage/delete_account/">\r\n\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-trash" aria-hidden="true"></span> Delete Account\r\n\t\t\t\t</a>\r\n\t\t\t</li>\r\n\t\t</ul>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"56": 50, "34": 1, "27": 0, "44": 3, "50": 3}, "source_encoding": "ascii", "filename": "C:\\Users\\Derek\\python\\test_dmp\\account\\templates/base.htm", "uri": "base.htm"}
__M_END_METADATA
"""
