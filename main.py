"""
Copyright 2024 Nekoweb Wiki

This software is licensed under the 3-clause BSD license.
You should have recieved a copy of such license with this software,
if you did not, a copy can be found at the following

    https://opensource.org/license/BSD-3-Clause

Otherwise, a copy of this license can be found in the root directory
of this project.
"""

from RenderUtils import JinjaRender, RenderMarkdown, WIKI_PAGE_TEMPLATE, TOC, GetTemplate, MDWiki
from os import listdir
from os.path import join as JoinPath, isdir, exists as PathExists
from MiscUtils import InitDir, IncludeExclude, IncludeExcludeTest, GenericCopy
from config import OUTPUT_DIR, DIRECTORIES, ADD_FILES
from distutils.dir_util import copy_tree as CopyDir

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
        ForcedTitle = RenderedMD.metadata["focetitle"] if "forcetitle" in RenderedMD.metadata else None
        TableOfContents = TOC(
                            RenderedMD.toc_html,
                            forcenone=(
                                (not isarticle) or
                                (RenderedMD.metadata["notoc"] if "notoc" in RenderedMD.metadata else False)
                            )
                          )
        RenderedOut = content.replace(".md", ".html")

        WikiRender = MDWiki(RenderedMD)
        JinjaRender(
            WIKI_PAGE_TEMPLATE,
            JoinPath(output, RenderedOut),
            PAGE_TITLE=f"Nekoweb Wiki - {PageTitle}" if ForcedTitle is None else ForcedTitle,
            PAGE_TYPE=("article" if isarticle else "website"),
            DisplayTitle=PageTitle,
            PAGE_DESC=PageSubtitle,
            TableOfContents=TableOfContents,
            Content=WikiRender,
            ShowPageInfo=True,
            Source=JoinPath(input_dir, content)
        )
        webout = output.replace("\\", "/").replace("build/", "/", 1) + "/" + RenderedOut

        if isarticle:
            Indexed.append((webout,PageTitle))

def StaticDirectory(directory: str, output: str):
    build_include, build_exclude = IncludeExclude(directory)

    for file in listdir(directory):
        CurrentPath = JoinPath(directory, file)
        FAILURE = IncludeExcludeTest(build_include, build_exclude, CurrentPath)
        if FAILURE:
            continue
        GenericCopy(CurrentPath, output)

def main():
    global Indexed
    InitDir(OUTPUT_DIR)

    for source, dest in ADD_FILES.items():
        GenericCopy(source, JoinPath(OUTPUT_DIR, dest))

    for directory, info in DIRECTORIES.items():
        output = JoinPath(OUTPUT_DIR, info["out"]).replace("\\", "/")

        if info["static"]:
            StaticDirectory(directory, output)
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
        ShowPageInfo=False,
    )

if __name__ == "__main__":
    main()

