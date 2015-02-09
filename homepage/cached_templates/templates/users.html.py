# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423503955.180399
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\Documents\\GitHub\\CHF\\test_dmp\\homepage\\templates/users.html'
_template_uri = 'users.html'
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
        users = context.get('users', UNDEFINED)
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
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t<h1>Users</h1>\r\n\t\t<table class="table table-striped table-bordered">\r\n\t\t<tr>\r\n\t\t\t<th>ID</th>\r\n\t\t\t<th>Username</th>\r\n\t\t\t<th>First Name</th>\r\n\t\t\t<th>Last Name</th>\r\n\t\t\t<th>Email</th>\r\n\t\t\t<th>City</th>\r\n\t\t\t<th>State</th>\r\n\t\t\t<th>Active</th>\r\n')
        if request.user.has_perm('homepage.is_admin'):
            __M_writer('\t\t\t\t<th>Actions</th>\r\n')
        __M_writer('\t\t<tr>\r\n')
        for user in users:
            __M_writer('\t\t\t<tr>\r\n\t\t\t\t<td>')
            __M_writer(str(user.id))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(user.username))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(user.first_name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(user.last_name))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(user.email))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(user.city))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(user.state))
            __M_writer('</td>\r\n\t\t\t\t<td>')
            __M_writer(str(user.is_active))
            __M_writer('</td>\r\n')
            if request.user.has_perm('homepage.is_admin'):
                __M_writer('\t\t\t\t\t<td>\r\n\t\t\t\t\t\t<a href="/homepage/users.edit/')
                __M_writer(str( user.id ))
                __M_writer('/">Edit</a>\r\n\t\t\t\t\t\t| \r\n\t\t\t\t\t\t<a href="/homepage/users.delete/')
                __M_writer(str( user.id ))
                __M_writer('/">Delete</a>\r\n\t\t\t\t\t</td>\r\n')
            __M_writer('\t\t\t<tr>\r\n')
        __M_writer('\t</table>\t\r\n\t<div class="text-right">\r\n\t\t<a class="btn btn-primary" href="/homepage/users.create/">Create New User</a>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Users\\Derek\\Documents\\GitHub\\CHF\\test_dmp\\homepage\\templates/users.html", "line_map": {"64": 23, "65": 23, "66": 24, "67": 24, "68": 25, "69": 25, "70": 26, "71": 26, "72": 27, "73": 27, "74": 28, "75": 28, "76": 29, "77": 30, "78": 31, "79": 31, "80": 33, "81": 33, "82": 36, "83": 38, "89": 83, "27": 0, "36": 1, "46": 3, "54": 3, "55": 15, "56": 16, "57": 18, "58": 19, "59": 20, "60": 21, "61": 21, "62": 22, "63": 22}, "uri": "users.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
