# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1557954964.0404599
_enable_loop = True
_template_filename = 'themes/foundation6/templates/post_helper.tmpl'
_template_uri = 'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['meta_translations', 'html_tags', 'html_pager', 'open_graph_metadata', 'twitter_card_information']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            for langname in sorted(translations):
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.tags:
            __M_writer('        <div class="callout secondary">\n        Tags:\n')
            for tag in post.tags:
                if tag not in hidden_tags:
                    __M_writer('            <span class="label"><a href="')
                    __M_writer(str(_link('tag', tag)))
                    __M_writer('" rel="tag">')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('</span></li>\n')
            __M_writer('        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.prev_post or post.next_post:
            __M_writer('        <div class="column row">\n            <ul class="pagination" role="navigation" aria-label="Pagination">\n')
            if post.prev_post:
                __M_writer('                <li>\n                    <a href="')
                __M_writer(str(post.prev_post.permalink()))
                __M_writer('" rel="prev" title="')
                __M_writer(filters.html_escape(str(post.prev_post.title())))
                __M_writer('">« <span class="show-for-sr">')
                __M_writer(str(messages("Previous post")))
                __M_writer('</span></a>\n                </li>\n')
            if post.next_post:
                __M_writer('                <li>\n                    <a href="')
                __M_writer(str(post.next_post.permalink()))
                __M_writer('" rel="next" title="')
                __M_writer(filters.html_escape(str(post.next_post.title())))
                __M_writer('" aria-label="Next page">» <span class="show-for-sr">')
                __M_writer(str(messages("Next post")))
                __M_writer('</span></a>\n                </li>\n')
            __M_writer('            </ul>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_open_graph_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        permalink = context.get('permalink', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<meta property="og:site_name" content="')
        __M_writer(filters.html_escape(str(blog_title)))
        __M_writer('">\n<meta property="og:title" content="')
        __M_writer(filters.html_escape(str(post.title()[:70])))
        __M_writer('">\n<meta property="og:url" content="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n')
        if post.description():
            __M_writer('    <meta property="og:description" content="')
            __M_writer(filters.html_escape(str(post.description()[:200])))
            __M_writer('">\n')
        else:
            __M_writer('    <meta property="og:description" content="')
            __M_writer(filters.html_escape(str(post.text(strip_html=True)[:200])))
            __M_writer('">\n')
        if post.previewimage:
            __M_writer('    <meta property="og:image" content="')
            __M_writer(str(url_replacer(permalink, post.previewimage, lang, 'absolute')))
            __M_writer('">\n')
        __M_writer('<meta property="og:type" content="article">\n')
        if post.date.isoformat():
            __M_writer('    <meta property="article:published_time" content="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('">\n')
        if post.tags:
            for tag in post.tags:
                __M_writer('       <meta property="article:tag" content="')
                __M_writer(filters.html_escape(str(tag)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_twitter_card_information(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if twitter_card and twitter_card['use_twitter_cards']:
            __M_writer('    <meta name="twitter:card" content="')
            __M_writer(filters.html_escape(str(twitter_card.get('card', 'summary'))))
            __M_writer('">\n')
            if 'site:id' in twitter_card:
                __M_writer('    <meta name="twitter:site:id" content="')
                __M_writer(str(twitter_card['site:id']))
                __M_writer('">\n')
            elif 'site' in twitter_card:
                __M_writer('    <meta name="twitter:site" content="')
                __M_writer(str(twitter_card['site']))
                __M_writer('">\n')
            if 'creator:id' in twitter_card:
                __M_writer('    <meta name="twitter:creator:id" content="')
                __M_writer(str(twitter_card['creator:id']))
                __M_writer('">\n')
            elif 'creator' in twitter_card:
                __M_writer('    <meta name="twitter:creator" content="')
                __M_writer(str(twitter_card['creator']))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/foundation6/templates/post_helper.tmpl", "uri": "post_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 11, "23": 24, "24": 43, "25": 70, "26": 86, "32": 3, "40": 3, "41": 4, "42": 5, "43": 6, "44": 7, "45": 7, "46": 7, "47": 7, "48": 7, "54": 13, "60": 13, "61": 14, "62": 15, "63": 17, "64": 18, "65": 19, "66": 19, "67": 19, "68": 19, "69": 19, "70": 22, "76": 26, "81": 26, "82": 27, "83": 28, "84": 30, "85": 31, "86": 32, "87": 32, "88": 32, "89": 32, "90": 32, "91": 32, "92": 35, "93": 36, "94": 37, "95": 37, "96": 37, "97": 37, "98": 37, "99": 37, "100": 40, "106": 45, "115": 45, "116": 46, "117": 46, "118": 47, "119": 47, "120": 48, "121": 48, "122": 49, "123": 50, "124": 50, "125": 50, "126": 51, "127": 52, "128": 52, "129": 52, "130": 54, "131": 55, "132": 55, "133": 55, "134": 57, "135": 62, "136": 63, "137": 63, "138": 63, "139": 65, "140": 66, "141": 67, "142": 67, "143": 67, "149": 72, "154": 72, "155": 73, "156": 74, "157": 74, "158": 74, "159": 75, "160": 76, "161": 76, "162": 76, "163": 77, "164": 78, "165": 78, "166": 78, "167": 80, "168": 81, "169": 81, "170": 81, "171": 82, "172": 83, "173": 83, "174": 83, "180": 174}}
__M_END_METADATA
"""
