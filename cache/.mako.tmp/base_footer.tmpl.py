# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1434557637.812691
_enable_loop = True
_template_filename = u'/usr/local/lib/python2.7/dist-packages/nikola/data/themes/base/templates/base_footer.tmpl'
_template_uri = u'base_footer.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_footer']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'base', context._clean_inheritance_tokens(), templateuri=u'base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'base')._populate(_import_ns, [u'*'])
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if content_footer:
            __M_writer(u'        <footer id="footer" role="contentinfo">\n            <p>')
            __M_writer(unicode(content_footer))
            __M_writer(u'</p>\n            ')
            __M_writer(unicode(template_hooks['page_footer']()))
            __M_writer(u'\n        </footer>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 2, "33": 11, "39": 4, "47": 4, "48": 5, "49": 6, "50": 7, "51": 7, "52": 8, "53": 8, "22": 2, "25": 0, "59": 53}, "uri": "base_footer.tmpl", "filename": "/usr/local/lib/python2.7/dist-packages/nikola/data/themes/base/templates/base_footer.tmpl"}
__M_END_METADATA
"""
