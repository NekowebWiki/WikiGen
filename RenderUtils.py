from markdown2 import markdown_path as INTERNAL_MD, UnicodeWithAttrs
from jinja2 import Environment as JINJA_ENV_INIT, \
                   FileSystemLoader as JINJA_LOADER, select_autoescape
from os import PathLike
from os.path import join as JoinPath
from jinja2.environment import Template as JINJA_TEMPLATE
from re import split as RegSplit, sub as RegSub
from config import LINK_PATTERS
from typing import Pattern as REGEXP

JinjaEnv = JINJA_ENV_INIT(
    loader=JINJA_LOADER("views"),
    autoescape=select_autoescape()
)

WIKI_PAGE_TEMPLATE = JinjaEnv.get_template("wikipage.html")

def GetTemplate(path) -> JINJA_TEMPLATE:
    return JinjaEnv.get_template(path)

def RenderMarkdown(path: str) -> UnicodeWithAttrs:
    """
    Returned value has 3 "states" (you could say):

    Val          (rendered md)
    Val.metadata (file metadata)
    Val.toc_html (table of contents)

    I'm mainly adding this note so I don't forget
    """
    Extras = {
        "toc": None,
        "metadata": None,
        "footnotes": None,
        "cuddled-lists": None,
        "fenced-code-blocks": None,
        "markdown-in-html": None,
        "strike": None,
        "tg-spoiler": None,
        "latex": None,
        "link-patterns": None,
    }
    Rendered = INTERNAL_MD(
        path, extras=Extras,
        link_patterns=LINK_PATTERS
    )
    return Rendered

def SubMulti(
    haystack: str,
    *needles: tuple[str | REGEXP, str]
) -> str:
    fin = haystack
    for needle, replace in needles:
        RegSub(needle, replace, fin)
    return fin

def MDWiki(RenderedMarkdown: str) -> str:
    ParsedOutput = SubMulti(
        RenderedMarkdown,
        (
            r"<sup class=\"footnote-ref\"",
            "<sup class=\"footnote-ref\" role=\"doc-noteref\""
        ),
        (
            r"<li id=\"fn-",
            "<li role=\"doc-footnote\" id=\"fn-",
        ),
        (
            r"<div class=\"footnotes\">\r?\n<hr \/>",
            "<div class=\"footnotes\">",
        ),
        (
            r"<tg-spoiler>",
            "<span class=\"spoiler\">",
        ),
        (
            r"</tg-spoiler>",
            "</span>",
        ),
    )
    return ParsedOutput

def TOC(toc_html: str | None, forcenone: bool = False) -> str | None:
    if toc_html is None or forcenone:
        return None
    ParsedTOC = toc_html[6:len(toc_html)-6].replace("<ul>", "<ol>").replace("</ul>", "</ol>")
    return ParsedTOC

def JinjaRender(
    templatein: JINJA_TEMPLATE,
    outpath: str | PathLike[str],
    **kwargs
):
    Rendered = templatein.render(**kwargs)
    with open(outpath, "x", encoding="utf-8") as f:
        f.write(Rendered)
