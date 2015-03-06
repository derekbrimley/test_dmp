# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425519341.031124
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\test_dmp\\account\\templates/login.html'
_template_uri = 'login.html'
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
        form = context.get('form', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<h1>User Login</h1><span id="id_username_message"></span>\r\n\t<div id="login_form_container">\r\n\t\t<form id="login_form" class="form-inline" action="/account/login.login_form/" method="POST">\r\n\t\t\t<table class="form-group">\r\n\t\t\t\t')
        __M_writer(str( form ))
        __M_writer('\r\n\t\t\t</table>\r\n\t\t\t<input type="submit" class="btn btn-default">\r\n\t\t</form>\r\n\t</div>\r\n\t\r\n\t<br/>\r\n\t<br/>\r\n\t<br/>\r\n\t<span id="text">\r\n\t\tDon\'t have an account?\r\n\t\t<!-- Button trigger modal -->\r\n\t\t<button type="button" class="btn btn-primary" id="create_user_dialog">\r\n\t\t  Click Here\r\n\t\t</button>\r\n\t</span>\r\n\t\r\n\t<!-- Modal -->\r\n\t<div class="modal fade" id="login_dialog" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">\r\n\t  <div class="modal-dialog">\r\n\t\t<div class="modal-content">\r\n\t\t  <div class="modal-header">\r\n\t\t\t<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>\r\n\t\t\t<h4 class="modal-title" id="myModalLabel">Create Account</h4>\r\n\t\t  </div>\r\n\t\t  <div class="modal-body">\r\n\t\t\t...\r\n\t\t  </div>\r\n\t\t  <div class="modal-footer">\r\n\t\t\t<button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\r\n\t\t\t<button type="button" class="btn btn-primary">Save changes</button>\r\n\t\t  </div>\r\n\t\t</div>\r\n\t  </div>\r\n\t</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"35": 1, "52": 3, "53": 8, "54": 8, "27": 0, "60": 54, "45": 3}, "uri": "login.html", "filename": "C:\\Users\\Derek\\python\\test_dmp\\account\\templates/login.html"}
__M_END_METADATA
"""
