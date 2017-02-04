# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1486222902.9515474
_enable_loop = True
_template_filename = 'themes/lanyon/templates/base_header.tmpl'
_template_uri = 'base_header.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_site_title', 'html_navigation_links', 'html_translation_header', 'html_header']


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


def render_html_site_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
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


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
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
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
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


def render_html_header(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        def html_site_title():
            return render_html_site_title(context)
        def html_navigation_links():
            return render_html_navigation_links(context)
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        def html_translation_header():
            return render_html_translation_header(context)
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
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
{"line_map": {"128": 6, "129": 6, "130": 7, "131": 7, "132": 8, "133": 8, "134": 9, "135": 10, "136": 11, "137": 11, "138": 14, "139": 15, "140": 15, "146": 140, "23": 2, "26": 0, "33": 2, "34": 16, "35": 22, "36": 32, "37": 42, "43": 18, "53": 18, "54": 20, "55": 20, "56": 20, "57": 20, "58": 20, "59": 20, "65": 24, "74": 24, "75": 26, "76": 27, "77": 27, "78": 27, "79": 27, "80": 27, "81": 29, "82": 29, "83": 29, "84": 30, "85": 30, "91": 35, "101": 35, "102": 36, "103": 37, "104": 38, "105": 38, "106": 39, "107": 39, "113": 4, "127": 4}, "source_encoding": "utf-8", "filename": "themes/lanyon/templates/base_header.tmpl", "uri": "base_header.tmpl"}
__M_END_METADATA
"""
