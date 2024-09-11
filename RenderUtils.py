"""
Copyright 2024 Nekoweb Wiki

This software is licensed under the 3-clause BSD license.
You should have recieved a copy of such license with this software,
if you did not, a copy can be found at the following

    https://opensource.org/license/BSD-3-Clause

Otherwise, a copy of this license can be found in the root directory
of this project.
"""

from markdown2 import markdown_path as INTERNAL_MD, UnicodeWithAttrs
from jinja2 import Environment as JINJA_ENV_INIT, \
                   FileSystemLoader as JINJA_LOADER, select_autoescape
from os import PathLike
from os.path import join as JoinPath
from jinja2.environment import Template as JINJA_TEMPLATE
from re import split as RegSplit, sub as RegSub, match as RegMatch
from typing import Pattern as REGEXP
from config import SOURCE_PREFIX, CODE_REPOSITORY, SOURCE_SUFFIX, COMMITS_PREFIX, COMMITS_SUFFIX, LINK_PATTERS
from minify_html import minify as MinHTML

JinjaEnv = JINJA_ENV_INIT(
    loader=JINJA_LOADER("views"),
    autoescape=select_autoescape()
)

JinjaEnv.globals["SourcePrefix"] = SOURCE_PREFIX
JinjaEnv.globals["SourceSuffix"] = SOURCE_SUFFIX
JinjaEnv.globals["CODE_REPOSITORY"] = CODE_REPOSITORY
JinjaEnv.globals["CommitsPrefix"] = COMMITS_PREFIX
JinjaEnv.globals["CommitsSuffix"] = COMMITS_SUFFIX

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
        "tables": None,
    }
    Rendered = INTERNAL_MD(
        path, extras=Extras,
        link_patterns=LINK_PATTERS
    )
    return Rendered

def SubMulti(
    haystack: str,
    *needles: tuple[str | REGEXP, str, str]
) -> str:
    fin = haystack
    matched: dict[str, bool] = {}
    for needle, replace, identity in needles:
        prefin = fin
        fin = RegSub(needle, replace, fin)
        matched[identity] = prefin != fin
    return fin, matched

def MDWiki(RenderedMarkdown: str, options: dict[str, str]) -> tuple[str, dict[str, any]]:
    ParsedOutput, matched = SubMulti(
        RenderedMarkdown,
        (
            r"<div class=\"footnotes\">\r?\n<hr \/>",
            "<div class=\"footnotes\">",
            "footnotes"
        ),
        (
            r"<tg-spoiler>",
            "<span class=\"spoiler\">",
            "tg-1"
        ),
        (
            r"</tg-spoiler>",
            "</span>",
            "tg-2"
        ),
        (
            r"<place-toc ?(?:/>|></place-toc>)",
            options["toc"] if options["toc"] is not None else "",
            "toc"
        ),
    )
    Options = {
        "manualtoc": matched["toc"]
    }
    return ParsedOutput, Options

def TOC(toc_html: str | None, forcenone: bool = False) -> str | None:
    if toc_html is None or forcenone:
        return None
    ParsedTOC = toc_html[6:len(toc_html)-6].replace("<ul>", "<ol>").replace("</ul>", "</ol>")
    return f"""
<nav class="table-of-contents">
    <h2>Contents</h2>
    <ol role="directory">
        {ParsedTOC}
    </ol>
</nav>"""


def JinjaRender(
    templatein: JINJA_TEMPLATE,
    outpath: str | PathLike[str],
    **kwargs
):
    Rendered = templatein.render(**kwargs)
    with open(outpath, "x", encoding="utf-8") as f:
        f.write(MinHTML(Rendered, keep_comments=True))
