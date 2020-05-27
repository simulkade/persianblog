# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1590597871.6445165
_enable_loop = True
_template_filename = 'themes/foundation6/templates/index_helper.tmpl'
_template_uri = 'index_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_pager']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if prevlink or nextlink:
            __M_writer('\n        <div class="column row">\n            <ul class="pagination" role="navigation" aria-label="Pagination">\n')
            if prevlink:
                __M_writer('                <li>\n                    <a href="')
                __M_writer(str(prevlink))
                __M_writer('" rel="prev">« <span class="show-for-sr">')
                __M_writer(str(messages("Newer posts")))
                __M_writer('</span></a>\n                </li>\n')
            if nextlink:
                __M_writer('                <li>\n                    <a href="')
                __M_writer(str(nextlink))
                __M_writer('" rel="next">» <span class="show-for-sr">')
                __M_writer(str(messages("Older posts")))
                __M_writer('</span></a>\n                </li>\n')
            __M_writer('            </ul>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/foundation6/templates/index_helper.tmpl", "uri": "index_helper.tmpl", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 20, "27": 2, "34": 2, "35": 3, "36": 4, "37": 7, "38": 8, "39": 9, "40": 9, "41": 9, "42": 9, "43": 12, "44": 13, "45": 14, "46": 14, "47": 14, "48": 14, "49": 17, "55": 49}}
__M_END_METADATA
"""
