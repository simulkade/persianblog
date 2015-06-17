# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1434557637.783526
_enable_loop = True
_template_filename = u'/usr/local/lib/python2.7/dist-packages/nikola/data/themes/base/templates/base_helper.tmpl'
_template_uri = u'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_translations', 'html_headstart', 'late_load_js', 'html_stylesheets', 'html_feedlinks']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    <ul class="translations">\n')
        for langname in translations.keys():
            if langname != lang:
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(abs_link(_link("root", None, langname))))
                __M_writer(u'" rel="alternate" hreflang="')
                __M_writer(unicode(langname))
                __M_writer(u'">')
                __M_writer(unicode(messages("LANGUAGE", langname)))
                __M_writer(u'</a></li>\n')
        __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        description = context.get('description', UNDEFINED)
        title = context.get('title', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        comment_system = context.get('comment_system', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html>\n<html ')
        __M_writer(u"prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer(u'og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer(u'fb: http://ogp.me/ns/fb#\n')
        __M_writer(u"' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer(u'vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer(u'dir="rtl" ')
        __M_writer(u'lang="')
        __M_writer(unicode(lang))
        __M_writer(u'">\n<head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer(u'    <meta name="description" content="')
            __M_writer(unicode(description))
            __M_writer(u'">\n')
        __M_writer(u'    <meta name="viewport" content="width=device-width">\n    <title>')
        __M_writer(striphtml(unicode(title)))
        __M_writer(u' | ')
        __M_writer(striphtml(unicode(blog_title)))
        __M_writer(u'</title>\n\n    ')
        __M_writer(unicode(html_stylesheets()))
        __M_writer(u'\n    ')
        __M_writer(unicode(html_feedlinks()))
        __M_writer(u'\n')
        if permalink:
            __M_writer(u'      <link rel="canonical" href="')
            __M_writer(unicode(abs_link(permalink)))
            __M_writer(u'">\n')
        __M_writer(u'\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer(u'            <link rel="')
                __M_writer(unicode(name))
                __M_writer(u'" href="')
                __M_writer(unicode(file))
                __M_writer(u'" sizes="')
                __M_writer(unicode(size))
                __M_writer(u'"/>\n')
        __M_writer(u'\n')
        if comment_system == 'facebook':
            __M_writer(u'        <meta property="fb:app_id" content="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'">\n')
        __M_writer(u'\n')
        if prevlink:
            __M_writer(u'        <link rel="prev" href="')
            __M_writer(unicode(prevlink))
            __M_writer(u'" type="text/html">\n')
        if nextlink:
            __M_writer(u'        <link rel="next" href="')
            __M_writer(unicode(nextlink))
            __M_writer(u'" type="text/html">\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(mathjax_config))
        __M_writer(u'\n')
        if use_cdn:
            __M_writer(u'        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer(u'        <!--[if lt IE 9]><script src="')
            __M_writer(unicode(url_replacer(permalink, '/assets/js/html5.js', lang)))
            __M_writer(u'"></script><![endif]-->\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(extra_head_data))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(social_buttons_code))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_bundles:
            if use_cdn:
                __M_writer(u'            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer(u'            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            __M_writer(u'        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer(u'            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer(u'        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if rss_link:
            __M_writer(u'        ')
            __M_writer(unicode(rss_link))
            __M_writer(u'\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer(u'                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('rss', None, language)))
                    __M_writer(u'">\n')
            else:
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(unicode(_link('rss', None)))
                __M_writer(u'">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in translations:
                    __M_writer(u'                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('index_atom', None, language)))
                    __M_writer(u'">\n')
            else:
                __M_writer(u'            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(unicode(_link('index_atom', None)))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"15": 0, "20": 2, "21": 61, "22": 65, "23": 86, "24": 109, "25": 119, "31": 111, "40": 111, "41": 113, "42": 114, "43": 115, "44": 115, "45": 115, "46": 115, "47": 115, "48": 115, "49": 115, "50": 118, "56": 3, "83": 3, "84": 6, "85": 7, "86": 8, "87": 10, "88": 11, "89": 13, "90": 14, "91": 15, "92": 17, "93": 18, "94": 21, "95": 21, "96": 21, "97": 24, "98": 25, "99": 25, "100": 25, "101": 27, "102": 28, "103": 28, "104": 28, "105": 28, "106": 30, "107": 30, "108": 31, "109": 31, "110": 32, "111": 33, "112": 33, "113": 33, "114": 35, "115": 36, "116": 37, "117": 38, "118": 38, "119": 38, "120": 38, "121": 38, "122": 38, "123": 38, "124": 41, "125": 42, "126": 43, "127": 43, "128": 43, "129": 45, "130": 46, "131": 47, "132": 47, "133": 47, "134": 49, "135": 50, "136": 50, "137": 50, "138": 52, "139": 53, "140": 53, "141": 54, "142": 55, "143": 56, "144": 57, "145": 57, "146": 57, "147": 59, "148": 60, "149": 60, "155": 63, "160": 63, "161": 64, "162": 64, "168": 67, "176": 67, "177": 68, "178": 69, "179": 70, "180": 71, "181": 72, "182": 74, "183": 75, "184": 78, "185": 79, "186": 82, "187": 83, "193": 88, "203": 88, "204": 89, "205": 90, "206": 90, "207": 90, "208": 91, "209": 92, "210": 93, "211": 94, "212": 94, "213": 94, "214": 94, "215": 94, "216": 96, "217": 97, "218": 97, "219": 97, "220": 100, "221": 101, "222": 102, "223": 103, "224": 103, "225": 103, "226": 103, "227": 103, "228": 105, "229": 106, "230": 106, "231": 106, "237": 231}, "uri": "base_helper.tmpl", "filename": "/usr/local/lib/python2.7/dist-packages/nikola/data/themes/base/templates/base_helper.tmpl"}
__M_END_METADATA
"""
