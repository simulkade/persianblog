# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1557954963.9921825
_enable_loop = True
_template_filename = 'themes/foundation6/templates/tags.tmpl'
_template_uri = 'tags.tmpl'
_source_encoding = 'utf-8'
_exports = ['page_header', 'content']


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
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        len = context.get('len', UNDEFINED)
        title = context.get('title', UNDEFINED)
        cat_hierarchy = context.get('cat_hierarchy', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        range = context.get('range', UNDEFINED)
        items = context.get('items', UNDEFINED)
        cat_items = context.get('cat_items', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def page_header():
            return render_page_header(context._locals(__M_locals))
        blog_description = context.get('blog_description', UNDEFINED)
        __M_writer = context.writer()
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


def render_page_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        def page_header():
            return render_page_header(context)
        blog_title = context.get('blog_title', UNDEFINED)
        blog_description = context.get('blog_description', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if title:
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</h1>\n    <h2>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h2>\n')
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
        len = context.get('len', UNDEFINED)
        cat_hierarchy = context.get('cat_hierarchy', UNDEFINED)
        range = context.get('range', UNDEFINED)
        items = context.get('items', UNDEFINED)
        cat_items = context.get('cat_items', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if cat_items:
            if items:
                __M_writer('            <h2>')
                __M_writer(str(messages("Categories")))
                __M_writer('</h2>\n')
            for text, full_name, path, link, indent_levels, indent_change_before, indent_change_after in cat_hierarchy:
                for i in range(indent_change_before):
                    __M_writer('                <ul class="postlist">\n')
                __M_writer('            <li><a class="reference" href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('</a>\n')
                if indent_change_after <= 0:
                    __M_writer('                </li>\n')
                for i in range(-indent_change_after):
                    __M_writer('                </ul>\n')
                    if i + 1 < len(indent_levels):
                        __M_writer('                    </li>\n')
            if items:
                __M_writer('            <h2>')
                __M_writer(str(messages("Tags")))
                __M_writer('</h2>\n')
        if items:
            __M_writer('        <div>\n')
            for text, link in items:
                if text not in hidden_tags:
                    __M_writer('                <span class="label large"><a href="')
                    __M_writer(str(link))
                    __M_writer('">')
                    __M_writer(filters.html_escape(str(text)))
                    __M_writer('</span>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/foundation6/templates/tags.tmpl", "uri": "tags.tmpl", "source_encoding": "utf-8", "line_map": {"27": 0, "46": 2, "51": 12, "56": 47, "62": 4, "71": 4, "72": 5, "73": 6, "74": 6, "75": 6, "76": 7, "77": 7, "78": 8, "79": 9, "80": 9, "81": 9, "82": 10, "83": 10, "89": 14, "102": 14, "103": 15, "104": 16, "105": 17, "106": 17, "107": 17, "108": 19, "109": 20, "110": 21, "111": 23, "112": 23, "113": 23, "114": 23, "115": 23, "116": 24, "117": 25, "118": 27, "119": 28, "120": 29, "121": 30, "122": 34, "123": 35, "124": 35, "125": 35, "126": 38, "127": 39, "128": 40, "129": 41, "130": 42, "131": 42, "132": 42, "133": 42, "134": 42, "135": 45, "141": 135}}
__M_END_METADATA
"""
