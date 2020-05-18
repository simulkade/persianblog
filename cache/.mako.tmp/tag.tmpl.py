# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1589829390.5168328
_enable_loop = True
_template_filename = 'themes/foundation6/templates/tag.tmpl'
_template_uri = 'tag.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'page_header', 'content']


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
    return runtime._inherit_from(context, 'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        generate_rss = context.get('generate_rss', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        description = context.get('description', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        subcategories = context.get('subcategories', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        len = context.get('len', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def page_header():
            return render_page_header(context._locals(__M_locals))
        date_format = context.get('date_format', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header'):
            context['self'].page_header(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        len = context.get('len', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if len(translations) > 1 and generate_rss:
            for language in sorted(translations):
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS for ')
                __M_writer(str(kind))
                __M_writer(' ')
                __M_writer(filters.html_escape(str(tag)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')" href="')
                __M_writer(str(_link(kind + "_rss", tag, language)))
                __M_writer('">\n')
        elif generate_rss:
            __M_writer('        <link rel="alternate" type="application/rss+xml" title="RSS for ')
            __M_writer(str(kind))
            __M_writer(' ')
            __M_writer(filters.html_escape(str(tag)))
            __M_writer('" href="')
            __M_writer(str(_link(kind + "_rss", tag)))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        def page_header():
            return render_page_header(context)
        blog_title = context.get('blog_title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<h1>')
        __M_writer(filters.html_escape(str(blog_title)))
        __M_writer('</h1>\n<h2>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h2>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        posts = context.get('posts', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        description = context.get('description', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<article class="tagpage">\n    <header>\n')
        if description:
            __M_writer('        <p>')
            __M_writer(str(description))
            __M_writer('</p>\n')
        if subcategories:
            __M_writer('        ')
            __M_writer(str(messages('Subcategories:')))
            __M_writer('\n        <ul>\n')
            for name, link in subcategories:
                __M_writer('            <li><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('        <div class="metadata">\n')
        if len(translations) > 1 and generate_rss:
            for language in sorted(translations):
                __M_writer('                <p class="feedlink">\n                    <a href="')
                __M_writer(str(_link(kind + "_rss", tag, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="application/rss+xml">')
                __M_writer(str(messages('RSS feed', language)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')</a>&nbsp;\n                </p>\n')
        elif generate_rss:
            __M_writer('                <p class="feedlink"><a href="')
            __M_writer(str(_link(kind + "_rss", tag)))
            __M_writer('" type="application/rss+xml">')
            __M_writer(str(messages('RSS feed')))
            __M_writer('</a></p>\n')
        __M_writer('        </div>\n    </header>\n')
        if posts:
            __M_writer('    <ul class="menu vertical">\n')
            for post in posts:
                __M_writer('        <li><time class="listdate" datetime="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('" title="')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('</time> <a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="listtitle">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('<a></li>\n')
            __M_writer('    </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/foundation6/templates/tag.tmpl", "uri": "tag.tmpl", "source_encoding": "utf-8", "line_map": {"27": 0, "53": 2, "58": 13, "63": 18, "68": 54, "74": 4, "88": 4, "89": 5, "90": 5, "91": 6, "92": 7, "93": 8, "94": 8, "95": 8, "96": 8, "97": 8, "98": 8, "99": 8, "100": 8, "101": 8, "102": 10, "103": 11, "104": 11, "105": 11, "106": 11, "107": 11, "108": 11, "109": 11, "115": 15, "123": 15, "124": 16, "125": 16, "126": 17, "127": 17, "133": 20, "151": 20, "152": 23, "153": 24, "154": 24, "155": 24, "156": 26, "157": 27, "158": 27, "159": 27, "160": 29, "161": 30, "162": 30, "163": 30, "164": 30, "165": 30, "166": 32, "167": 34, "168": 35, "169": 36, "170": 37, "171": 38, "172": 38, "173": 38, "174": 38, "175": 38, "176": 38, "177": 38, "178": 38, "179": 41, "180": 42, "181": 42, "182": 42, "183": 42, "184": 42, "185": 44, "186": 46, "187": 47, "188": 48, "189": 49, "190": 49, "191": 49, "192": 49, "193": 49, "194": 49, "195": 49, "196": 49, "197": 49, "198": 49, "199": 49, "200": 51, "201": 53, "207": 201}}
__M_END_METADATA
"""
