# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1495964840.9821932
_enable_loop = True
_template_filename = 'themes/lanyon/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_navigation_links', 'html_translation_header', 'html_site_title', 'html_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <nav id="menu" role="navigation" class="sidebar-nav">\n')
        for url, text in navigation_links[lang]:
            __M_writer('        <a class="sidebar-nav-item" href="')
            __M_writer(str(url))
            __M_writer('">')
            __M_writer(str(text))
            __M_writer('</a>\n')
        __M_writer('    ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n    ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translation_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        base = _mako_get_namespace(context, 'base')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('        <div id="toptranslations">\n            <h2>')
            __M_writer(str(messages("Languages:")))
            __M_writer('</h2>\n            ')
            __M_writer(str(base.html_translations()))
            __M_writer('\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <h3 id="brand" class="masthead-title">\n      <a href="')
        __M_writer(str(abs_link(_link("root", None, lang))))
        __M_writer('" title="')
        __M_writer(str(blog_title))
        __M_writer('" rel="home">')
        __M_writer(str(blog_title))
        __M_writer('</a>\n    </h3>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        def html_navigation_links():
            return render_html_navigation_links(context)
        def html_translation_header():
            return render_html_translation_header(context)
        def html_site_title():
            return render_html_site_title(context)
        __M_writer = context.writer()
        __M_writer('\n    <header id="header" role="banner">\n        ')
        __M_writer(str(html_site_title()))
        __M_writer('\n        ')
        __M_writer(str(html_translation_header()))
        __M_writer('\n        ')
        __M_writer(str(html_navigation_links()))
        __M_writer('\n')
        if search_form:
            __M_writer('            <div class="searchform" role="search">\n                ')
            __M_writer(str(search_form))
            __M_writer('\n            </div>\n')
        __M_writer('    </header>\n    ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 6, "129": 6, "130": 7, "131": 7, "132": 8, "133": 8, "134": 9, "135": 10, "136": 11, "137": 11, "138": 14, "139": 15, "140": 15, "146": 140, "23": 2, "26": 0, "33": 2, "34": 16, "35": 22, "36": 32, "37": 42, "43": 24, "52": 24, "53": 26, "54": 27, "55": 27, "56": 27, "57": 27, "58": 27, "59": 29, "60": 29, "61": 29, "62": 30, "63": 30, "69": 35, "79": 35, "80": 36, "81": 37, "82": 38, "83": 38, "84": 39, "85": 39, "91": 18, "101": 18, "102": 20, "103": 20, "104": 20, "105": 20, "106": 20, "107": 20, "113": 4, "127": 4}, "filename": "themes/lanyon/templates/base_header.tmpl", "source_encoding": "utf-8", "uri": "base_header.tmpl"}
__M_END_METADATA
"""
