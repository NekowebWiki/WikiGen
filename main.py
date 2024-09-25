"""
Copyright 2024 Nekoweb Wiki

This software is licensed under the 3-clause BSD license.
You should have recieved a copy of such license with this software,
if you did not, a copy can be found at the following

    https://opensource.org/license/BSD-3-Clause

Otherwise, a copy of this license can be found in the root directory
of this project.
"""
from git import Repo
from RenderUtils import JinjaRender, RenderMarkdown, WIKI_PAGE_TEMPLATE, TOC, GetTemplate, MDWiki
from os import listdir
from os.path import join as JoinPath, isdir, exists as PathExists, dirname, realpath
from MiscUtils import InitDir, IncludeExclude, IncludeExcludeTest, GenericCopy
from config import OUTPUT_DIR, DIRECTORIES, ADD_FILES, COMMIT_PREFIX, COMMIT_SUFFIX, SITE_URL
from distutils.dir_util import copy_tree as CopyDir
from syntaxcolors import AddSyntaxColors
from datetime import datetime, UTC as UTC_TIMESTAMP

repo = Repo()

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
        metadata = RenderedMD.metadata

        PageTitle = metadata["title"]
        Title = (
                    metadata["forcetitle"]
                    if "forcetitle" in metadata
                    else f"Nekoweb Wiki - {PageTitle}"
                )

        PageSubtitle = metadata["subtitle"] if "subtitle" in metadata else None
        Description = metadata["desc"] if "desc" in metadata else PageSubtitle

        TableOfContents = TOC(
                              RenderedMD.toc_html,
                              forcenone=(
                                  metadata["notoc"] if "notoc" in metadata else False
                              )
                          )
        RenderedOut = content.replace(".md", ".html")
        
        WikiRender, options = MDWiki(
                RenderedMD,
                {
                    "toc": TableOfContents,
                }
            )
        JinjaRender(
            WIKI_PAGE_TEMPLATE,
            JoinPath(output, RenderedOut),
            LANG="en",
            PAGE_TITLE=Title,
            PAGE_TYPE=("article" if isarticle else "website"),
            DisplayTitle=PageTitle,
            PAGE_DESC=Description,
            PAGE_SUBTITLE=PageSubtitle,
            TableOfContents=TableOfContents if not options["manualtoc"] else None,
            Content=WikiRender,
            Source=JoinPath(input_dir, content).replace("\\", "/")
        )
        webout = output.replace("\\", "/").replace("build/", "/", 1) + "/" + RenderedOut

        Indexed.append((webout,PageTitle,input_dir,Description))

def StaticDirectory(directory: str, output: str):
    build_include, build_exclude = IncludeExclude(directory)

    for file in listdir(directory):
        CurrentPath = JoinPath(directory, file)
        FAILURE = IncludeExcludeTest(build_include, build_exclude, CurrentPath)
        if FAILURE:
            continue
        GenericCopy(CurrentPath, output)

def WriteFeed(CommitBase, ReleaseMessage = "#action/build-deploy"):
    commits = list(CommitBase)

    Releases = []

    RSSFeed = ""
    for commit in commits:
        if len(Releases) == 10:
            break
        if ReleaseMessage not in commit.message:
            continue
        ChangelogId = datetime.fromtimestamp(commit.authored_date, UTC_TIMESTAMP).strftime("%Y-%b-%d").lower()
        if ChangelogId in Releases:
            continue
        Releases.append(ChangelogId)

        author = commit.author.name
        date = datetime.fromtimestamp(commit.authored_date, UTC_TIMESTAMP).strftime("%a, %d %b %Y %H:%M:%S GMT")

        commitlink = SITE_URL + "changelog.html#" + ChangelogId
        
        RSSFeed += \
            "<item>" +\
                f"<title>Site update!</title>" +\
                f"<link>{commitlink}</link>" +\
                f"<description>See link for details.</description>" +\
                f"<pubDate>{date}</pubDate>" +\
                f"<guid>{ChangelogId}</guid>" +\
            "</item>"
    RSSFeed = \
    "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>" +\
    "<rss version=\"2.0\">" +\
        "<channel>" +\
            "<title>Nekoweb Wiki</title>" +\
           f"<link>{SITE_URL}</link>" +\
            "<lang>en-us</lang>" +\
            RSSFeed +\
        "</channel>" +\
    "</rss>"
    return RSSFeed


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
        PAGE_TITLE = "Nekoweb Wiki - Page Index",
        PAGE_DESC = "A list of pages on this wiki.",
        PAGE_TYPE = "website",
        LANG="en",
        pages = Indexed,
    )
    JinjaRender(
        GetTemplate("guestbook.html"),
        JoinPath("build", "guestbook.html"),
        PAGE_TITLE = "Nekoweb Wiki - Guestbook",
        PAGE_DESC = "Sign the wiki guestbook!",
        PAGE_TYPE = "website",
        LANG="en",
    )
    JinjaRender(
        GetTemplate("editor.html"),
        JoinPath("build", "editor.html"),
        PAGE_TITLE = "Nekoweb Wiki - Edit!",
        PAGE_DESC = "(experimental) Edit wikipages!",
        PAGE_TYPE = "website",
        LANG="en",
    )
    AddSyntaxColors()

    RSSFeed = WriteFeed(
        CommitBase = repo.iter_commits("HEAD", max_count=50)
    )
    with open(JoinPath(OUTPUT_DIR, "feed.xml"), "w", encoding="utf-8") as file:
        file.write(RSSFeed)

if __name__ == "__main__":
    main()

