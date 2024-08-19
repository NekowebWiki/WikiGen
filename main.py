"""
    This is a small static site generator written to generate the Nekoweb Wiki: <https://wiki.nekoweb.org>.
    Copyright (C) 2024  Steve0Greatness

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from RenderUtils import JinjaRender, RenderMarkdown, WIKI_PAGE_TEMPLATE, TOC, GetTemplate, MDWiki
from os import listdir
from os.path import join as JoinPath, isdir
from MiscUtils import InitDir
from config import OUTPUT_DIR, SOURCE_PREFIX, CODE_REPOSITORY, SOURCE_SUFFIX
from distutils.dir_util import copy_tree as CopyDir

DIRECTORIES = {
    "static": {
        "out": "",
        "static": True
    },
    "content": {
        "out": "w",
        "static": False,
        "articledir": True
    },
    "headpages": {
        "out": "",
        "static": False,
        "articledir": False
    },
    "images": {
        "out": "i",
        "static": True
    }
}

Indexed = []

def wikiparse(input_dir: str, output: str, rawinfo: dict = { "out": "w", "articledir": True }):
    global Indexed
    contents = listdir(input_dir)
    for content in contents:
        if isdir(content):
            wikiparse(JoinPath(input_dir, content), JoinPath(output, content), rawinfo=rawinfo)
            continue
        isarticle = rawinfo["articledir"]
        RenderedMD = RenderMarkdown(JoinPath(input_dir, content))
        PageTitle = RenderedMD.metadata["title"]
        PageSubtitle = RenderedMD.metadata["subtitle"] if "subtitle" in RenderedMD.metadata else None
        TableOfContents = TOC(
                            RenderedMD.toc_html,
                            forcenone=(
                                (not isarticle) or
                                (RenderedMD.metadata["notoc"] if "notoc" in RenderedMD.metadata else False)
                          ))
        RenderedOut = content.replace(".md", ".html")
        WikiRender = MDWiki(RenderedMD)
        JinjaRender(
            WIKI_PAGE_TEMPLATE,
            JoinPath(output, RenderedOut),
            PAGE_TITLE=f"Nekoweb Wiki - {PageTitle}",
            PAGE_TYPE=("article" if isarticle else "website"),
            DisplayTitle=PageTitle,
            PAGE_DESC=PageSubtitle,
            TableOfContents=TableOfContents,
            Content=WikiRender,
            SourcePrefix=SOURCE_PREFIX,
            Source=JoinPath(input_dir, content),
            SourceSuffix=SOURCE_SUFFIX,
            CODE_REPOSITORY=CODE_REPOSITORY
        )

        webout = output.replace("\\", "/").replace("build/", "/", 1) + "/" + RenderedOut

        if isarticle:
            Indexed.append((webout,PageTitle))

def main():
    global Indexed
    InitDir(OUTPUT_DIR)

    for directory, info in DIRECTORIES.items():
        output = JoinPath(OUTPUT_DIR, info["out"]).replace("\\", "/")

        if info["static"]:
            CopyDir(directory, output)
            continue

        InitDir(output, overwrite=False)

        wikiparse(directory, output, rawinfo=info)
    JinjaRender(
        GetTemplate("pageindex.html"),
        JoinPath("build", "pages.html"),
        PAGE_TITLE = "Page Index",
        PAGE_DESCRIPTION = "A list of pages on this wiki.",
        PAGE_TYPE = "website",
        pages = Indexed,
        SourcePrefix=SOURCE_PREFIX,
        Source="main.py",
        SourceSuffix=SOURCE_SUFFIX,
        CODE_REPOSITORY=CODE_REPOSITORY
    )

if __name__ == "__main__":
    main()

