# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425592411.992086
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/base.htm'
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
        request = context.get('request', UNDEFINED)
        static_renderer = context.get('static_renderer', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n\t<body>\r\n\t\t<div class="container-fluid"\r\n\t\t\t<div class="row">\r\n\t\t\t\t<div class="col-md-2 left-menu">\r\n\t\t\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav'):
            context['self'].nav(**pageargs)
        

        __M_writer('\r\n\t\t\t\t</div>\t\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</body>\t\r\n</html>\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def nav():
            return render_nav(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t\t\t\t\t<div class="sidebar-nav">\r\n\t\t\t\t\t\t  <ul class="nav nav-pills nav-stacked">\r\n\t\t\t\t\t\t\t<li role="presentation" class="active">\r\n\t\t\t\t\t\t\t<a href="/homepage/">\r\n\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-home" aria-hidden="true"></span> Home\r\n\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t<a href="/homepage/products/">\r\n\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-gift" aria-hidden="true"></span> Products\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t<a href="/catalog/products/">\r\n\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-tag" aria-hidden="true"></span> Store\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</li>\r\n')
        if request.user.has_perm('homepage.is_manager'):
            __M_writer('\t\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t\t<a href="/homepage/items/">\r\n\t\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-th-list" aria-hidden="true"></span> Items\r\n\t\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t\t<a href="/homepage/users/">\r\n\t\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-user" aria-hidden="true"></span> Users\r\n\t\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t\t<a href="/homepage/transactions/">\r\n\t\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-time" aria-hidden="true"></span> Transactions\r\n\t\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t\t<!-- <li role="presentation">\r\n\t\t\t\t\t\t\t\t<a href="/homepage/orders/">\r\n\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-shopping-cart" aria-hidden="true"></span> Orders\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t\t</li> -->\r\n')
        __M_writer('\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t<a href="/homepage/events/">\r\n\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-calendar" aria-hidden="true"></span> Events\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t<a href="/homepage/about/">\r\n\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-bullhorn" aria-hidden="true"></span> About Us\t\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t<a href="/homepage/contact/">\r\n\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-comment" aria-hidden="true"></span> Contact\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t\t<li role="presentation">\r\n\t\t\t\t\t\t\t\t<a href="/homepage/Terms/">\r\n\t\t\t\t\t\t\t\t\t<span id="nav-glyphicon" class="glyphicon glyphicon-th" aria-hidden="true"></span> Terms\r\n\t\t\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t\t</li>\r\n\t\t\t\t\t\t  </ul>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"49": 9, "43": 79, "36": 1, "59": 49, "57": 27, "56": 9, "41": 71, "42": 79, "27": 0, "58": 28, "65": 59}, "filename": "C:\\Users\\Derek\\python\\test_dmp\\homepage\\templates/base.htm", "uri": "base.htm"}
__M_END_METADATA
"""
