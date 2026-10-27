# markdown_to_wechat_html.py

"""
简单的 Markdown 转换器，用于将文章 Markdown 转换为微信公众号兼容的 HTML。

微信公众平台的编辑器不支持复杂的 CSS 和 class，推荐使用行内样式或仅保留基础 HTML 标签。
此转换器实现了最基础的 Markdown 解析：标题（#、##、###）、段落、无序列表（-）、引用（>）、图片标记 (![]())。

注意：图片标记的 src 将被保留为原始字符串，请在发布流程中将其替换为微信图床返回的 URL。
"""

import html as html_lib
from typing import List
import re


BODY_STYLE = (
    "font-size:18px;line-height:2.05;margin:0 0 24px 0;"
    "color:#24302f;letter-spacing:0;"
)
LIST_WRAP_STYLE = "margin:0 0 26px 0;"
LIST_ROW_STYLE = (
    "font-size:18px;line-height:2.0;margin:0 0 14px 0;color:#24302f;"
    "letter-spacing:0;"
)
LIST_MARK_STYLE = (
    "display:inline-block;width:28px;min-width:28px;color:#d68b2c;"
    "font-weight:700;vertical-align:top;"
)
LIST_TEXT_STYLE = "display:inline;vertical-align:top;"
DOT_MARK_STYLE = "color:#24302f;"
H1_STYLE = (
    "display:inline-block;font-size:26px;line-height:1.45;font-weight:700;"
    "margin:8px 0 30px 0;color:#162826;background:#fff1a8;"
    "padding:6px 12px;border-radius:4px;"
)
H2_STYLE = (
    "font-size:23px;line-height:1.55;font-weight:700;margin:40px 0 18px 0;"
    "color:#163b35;border-left:5px solid #d68b2c;padding-left:12px;"
)
H3_STYLE = (
    "font-size:20px;line-height:1.55;font-weight:700;margin:30px 0 16px 0;"
    "color:#23413d;background:#f4faf7;padding:5px 10px;border-radius:4px;"
)
HR_STYLE = "border:0;border-top:1px solid #d8c79a;margin:34px 0;"
QUOTE_STYLE = (
    "margin:26px 0;padding:14px 16px;border-left:4px solid #d68b2c;"
    "background:#fff6df;color:#4a3725;font-size:18px;line-height:2.0;"
)
IMG_WRAP_STYLE = "margin:26px 0;text-align:center;"
IMG_STYLE = "width:100%;max-width:900px;height:auto;display:block;margin:0 auto;border-radius:6px;"
STRONG_STYLE = "font-weight:700;color:#0f5f52;background:#e9f7f1;padding:0 3px;border-radius:3px;"
HIGHLIGHT_STYLE = "background:#fff1a8;color:#26302f;padding:0 4px;border-radius:3px;"
UNDERLINE_STYLE = "text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:4px;color:#145f71;"
WAVY_STYLE = "text-decoration:underline wavy #d36b43;text-underline-offset:4px;color:#6a3223;"
EM_STYLE = "font-style:normal;color:#6b4a13;background:#fff7d6;padding:0 3px;border-radius:3px;"


def render_list_item(marker: str, text: str) -> str:
    """Render a list item without ul/li so WeChat edit mode cannot split marker and text."""
    marker_style = LIST_MARK_STYLE
    if marker == '•':
        marker_style += DOT_MARK_STYLE
    return (
        f'<p style="{LIST_ROW_STYLE}">'
        f'<span style="{marker_style}">{marker}</span>'
        f'<span style="{LIST_TEXT_STYLE}">{render_inline(text)}</span>'
        f'</p>'
    )


def render_inline(text: str) -> str:
    """Escape raw input, render HTTP(S) source links and supported emphasis."""
    links = []
    def save_link(match):
        label = html_lib.escape(match.group(1), quote=True)
        url = html_lib.escape(match.group(2), quote=True)
        links.append(f'<a href="{url}">{label}</a>')
        return "\x00LINK" + str(len(links) - 1) + "\x00"
    text = re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)', save_link, text)
    text = html_lib.escape(text, quote=True)
    for pattern, tag in [
        (r'==(.+?)==', f'<span style="{HIGHLIGHT_STYLE}">'),
        (r'\+\+(.+?)\+\+', f'<span style="{UNDERLINE_STYLE}">'),
        (r'~~(.+?)~~', f'<span style="{WAVY_STYLE}">'),
        (r'\*\*(.+?)\*\*', f'<strong style="{STRONG_STYLE}">'),
        (r'__(.+?)__', f'<strong style="{STRONG_STYLE}">'),
        (r'\*(.+?)\*', f'<em style="{EM_STYLE}">'),
        (r'_(.+?)_', f'<em style="{EM_STYLE}">'),
    ]:
        closing = "</" + tag.split()[0][1:] + ">"
        text = re.sub(pattern, lambda m, t=tag, c=closing: t + m.group(1) + c, text)
    for index, link in enumerate(links):
        text = text.replace("\x00LINK" + str(index) + "\x00", link)
    return text


def markdown_to_html(md_text: str) -> str:
    """
    将简单 Markdown 文本转换为微信公众号兼容的 HTML 字符串。

    :param md_text: 输入 Markdown 字符串
    :return: 输出 HTML 字符串（含基础内联样式）
    """
    lines = md_text.split("\n")
    html_lines: List[str] = []
    in_list = False

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            html_lines.append('</section>')
            in_list = False

    for line in lines:
        stripped = line.strip()
        if re.fullmatch(r'(-{3,}|\*{3,}|_{3,})', stripped):
            close_list()
            html_lines.append(f'<hr style="{HR_STYLE}"/>')
        elif stripped.startswith('### '):
            close_list()
            html_lines.append(f'<h3 style="{H3_STYLE}">{render_inline(stripped[4:].strip())}</h3>')
        elif stripped.startswith('## '):
            close_list()
            html_lines.append(f'<h2 style="{H2_STYLE}">{render_inline(stripped[3:].strip())}</h2>')
        elif stripped.startswith('# '):
            close_list()
            html_lines.append(f'<h1 style="{H1_STYLE}">{render_inline(stripped[2:].strip())}</h1>')
        elif stripped.startswith('- '):
            if not in_list:
                html_lines.append(f'<section style="{LIST_WRAP_STYLE}">')
                in_list = True
            html_lines.append(render_list_item('→', stripped[2:].strip()))
        elif re.match(r'^[•●]\s+', stripped):
            if not in_list:
                html_lines.append(f'<section style="{LIST_WRAP_STYLE}">')
                in_list = True
            html_lines.append(render_list_item('•', re.sub(r'^[•●]\s+', '', stripped, count=1).strip()))
        elif stripped.startswith('→ '):
            if not in_list:
                html_lines.append(f'<section style="{LIST_WRAP_STYLE}">')
                in_list = True
            html_lines.append(render_list_item('→', stripped[2:].strip()))
        elif stripped.startswith('>'):
            close_list()
            html_lines.append(f'<blockquote style="{QUOTE_STYLE}">{render_inline(stripped[1:].strip())}</blockquote>')
        elif stripped.startswith('!['):
            close_list()
            # 图片标签，保留 alt 和原始 url，后续由发布流程替换
            match = re.match(r'!\[(.*?)\]\((.*?)\)', stripped)
            if match:
                alt = html_lib.escape(match.group(1), quote=True)
                src = html_lib.escape(match.group(2), quote=True)
                html_lines.append(f'<p style="{IMG_WRAP_STYLE}"><img src="{src}" alt="{alt}" style="{IMG_STYLE}"/></p>')
        elif stripped == '':
            close_list()
            html_lines.append('')
        else:
            close_list()
            paragraph = render_inline(stripped)
            html_lines.append(f'<p style="{BODY_STYLE}">{paragraph}</p>')
    close_list()
    # 拼接为单个 HTML 字符串
    body_html = '\n'.join(html_lines)
    # 简单包装为完整 HTML
    return f'<div style="max-width:900px;margin:0 auto;color:#24302f;">{body_html}</div>'


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python markdown_to_wechat_html.py <markdown_file>")
        sys.exit(1)
    md_path = sys.argv[1]
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    html = markdown_to_html(md_text)
    print(html)
