# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425790596.720184
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'nav']


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
        static_renderer = context.get('static_renderer', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def nav():
            return render_nav(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n<header>\r\n  Welcome to the catalog app!\r\n</header>\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \r\n\r\n<div class="container-fluid"\r\n\t\t\t<div class="row">\r\n\t\t\t\t<div class="col-md-2 left-menu">\r\n\t\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav'):
            context['self'].nav(**pageargs)
        

        __M_writer('\r\n\t\t\t\t</div>\t\r\n\t\t\t</div>\r\n\t\t</div>\r\n\r\n')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n  Site content goes here in sub-templates.\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def nav():
            return render_nav(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t\t\t\t\t<div class="sidebar-nav">\r\n\t\t\t\t\t\t  <ul class="nav nav-pills nav-stacked">\r\n\t\t\t\t\t\t\t<li role="presentation" class="active">\r\n\t\t\t\t\t\t\t<a href="/homepage/">\r\n\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-arrow-left" aria-hidden="true"></span> Back Home\r\n\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t<a href="/catalog/products/">\r\n\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-search" aria-hidden="true"></span> Store\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t\t<a href="/catalog/items/">\r\n\t\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-filter" aria-hidden="true"></span> Categories\r\n\t\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t\t<a href="/catalog/products.checkout/">\r\n\t\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span> Shopping Cart\r\n\t\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t  </ul>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"48": 40, "49": 46, "50": 46, "27": 0, "68": 15, "38": 1, "56": 8, "80": 74, "74": 15, "43": 10, "62": 8}, "filename": "C:\\Users\\Derek\\python\\test_dmp\\catalog\\templates/base.htm", "uri": "base.htm"}
__M_END_METADATA
"""
