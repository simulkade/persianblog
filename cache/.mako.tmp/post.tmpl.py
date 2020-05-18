# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1589829390.8613594
_enable_loop = True
_template_filename = 'themes/foundation6/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'page_header', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('pheader', context._clean_inheritance_tokens(), templateuri='post_header.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pheader')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        blog_description = context.get('blog_description', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        parent = context.get('parent', UNDEFINED)
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        math = _mako_get_namespace(context, 'math')
        helper = _mako_get_namespace(context, 'helper')
        blog_title = context.get('blog_title', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        def page_header():
            return render_page_header(context._locals(__M_locals))
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
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
        post = context.get('post', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        math = _mako_get_namespace(context, 'math')
        parent = context.get('parent', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('    <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        if post.description():
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(post.description())))
            __M_writer('">\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(filters.html_escape(str(post.author())))
        __M_writer('">\n')
        if post.prev_post:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(post.prev_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.prev_post.title())))
            __M_writer('" type="text/html">\n')
        if post.next_post:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(post.next_post.permalink()))
            __M_writer('" title="')
            __M_writer(filters.html_escape(str(post.next_post.title())))
            __M_writer('" type="text/html">\n')
        if post.is_draft:
            __M_writer('        <meta name="robots" content="noindex">\n')
        __M_writer('    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n    ')
        __M_writer(str(math.math_styles_ifpost(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        blog_description = context.get('blog_description', UNDEFINED)
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        def page_header():
            return render_page_header(context)
        date_format = context.get('date_format', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</h1>\n    <h2 class="subheader"><small>')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</small></h2>\n')
        else:
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</h1>\n    <h2 class="subheader">')
            __M_writer(filters.html_escape(str(blog_description)))
            __M_writer('</h2>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        math = _mako_get_namespace(context, 'math')
        helper = _mako_get_namespace(context, 'helper')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        post = context.get('post', UNDEFINED)
        pheader = _mako_get_namespace(context, 'pheader')
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="blog-post">\n    ')
        __M_writer(str(pheader.html_post_header()))
        __M_writer('\n    ')
        __M_writer(str(post.text()))
        __M_writer('\n\n    <div class="callout">\n    <ul class="menu simple">\n')
        if author_pages_generated:
            __M_writer('        <li>Author: <a href="')
            __M_writer(str(_link('author', post.author())))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('</a></li>\n')
        else:
            __M_writer('        <li>Author: ')
            __M_writer(filters.html_escape(str(post.author())))
            __M_writer('</li>\n')
        __M_writer('\n')
        if post.meta('link'):
            __M_writer('        <li><a href="')
            __M_writer(str(post.meta('link')))
            __M_writer('">')
            __M_writer(str(messages("Original site")))
            __M_writer('</a></li>\n')
        __M_writer('    </ul>\n\n    </div>\n    ')
        __M_writer(str(helper.html_tags(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.html_pager(post)))
        __M_writer('\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('        ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n')
        __M_writer('    ')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n</div>\n')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/foundation6/templates/post.tmpl", "uri": "post.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "38": 0, "63": 2, "64": 3, "65": 4, "66": 5, "67": 6, "72": 30, "77": 40, "82": 69, "88": 8, "98": 8, "99": 9, "100": 9, "101": 10, "102": 11, "103": 11, "104": 11, "105": 13, "106": 14, "107": 14, "108": 14, "109": 16, "110": 16, "111": 16, "112": 17, "113": 18, "114": 18, "115": 18, "116": 18, "117": 18, "118": 20, "119": 21, "120": 21, "121": 21, "122": 21, "123": 21, "124": 23, "125": 24, "126": 26, "127": 26, "128": 26, "129": 27, "130": 27, "131": 28, "132": 28, "133": 29, "134": 29, "140": 32, "151": 32, "152": 33, "153": 34, "154": 34, "155": 34, "156": 35, "157": 35, "158": 36, "159": 37, "160": 37, "161": 37, "162": 38, "163": 38, "169": 42, "184": 42, "185": 44, "186": 44, "187": 45, "188": 45, "189": 49, "190": 50, "191": 50, "192": 50, "193": 50, "194": 50, "195": 51, "196": 52, "197": 52, "198": 52, "199": 54, "200": 55, "201": 56, "202": 56, "203": 56, "204": 56, "205": 56, "206": 58, "207": 61, "208": 61, "209": 62, "210": 62, "211": 63, "212": 64, "213": 64, "214": 64, "215": 66, "216": 66, "217": 66, "218": 68, "219": 68, "225": 219}}
__M_END_METADATA
"""
