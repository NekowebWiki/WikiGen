from RenderUtils import JinjaRender, RenderMarkdown, WIKI_PAGE_TEMPLATE, TOC
from os import listdir
from os.path import join as JoinPath, isdir
from MiscUtils import InitDir
from config import OUTPUT_DIR
from distutils.dir_util import copy_tree as CopyDir

DIRECTORIES = {
    "static": {
        "out": "",
        "static": True
    },
    "content": {
        "out": "w",
        "static": False,
        "indexdir": True,
        "articledir": True
    },
    "headpages": {
        "out": "",
        "static": False,
        "indexdir": False,
        "articledir": False
    },
    "images": {
        "out": "i",
        "static": True
    }
}

DirsIndexed = {}

def wikiparse(input_dir: str, output: str, isarticle: bool = True):
    contents = listdir(input_dir)
    for content in contents:
        if isdir(content):
            wikiparse(JoinPath(input_dir, content), JoinPath(output, content))
            continue
        RenderedMD = RenderMarkdown(JoinPath(input_dir, content))
        PageTitle = RenderedMD.metadata["title"]
        PageSubtitle = RenderedMD.metadata["subtitle"]
        TableOfContents = TOC(RenderedMD.toc_html)
        RenderedOut = content.replace(".md", ".html")
        JinjaRender(
            WIKI_PAGE_TEMPLATE,
            JoinPath(output, RenderedOut),
            PAGE_TITLE=f"Nekoweb Wiki - {PageTitle}",
            PAGE_TYPE=("article" if isarticle else "website"),
            DisplayTitle=PageTitle,
            PAGE_DESC=PageSubtitle,
            TableOfContents=TableOfContents,
            Content=RenderedMD
        )

def main():
    InitDir(OUTPUT_DIR)

    for directory, info in DIRECTORIES.items():
        output = JoinPath(OUTPUT_DIR, info["out"]).replace("\\", "/")

        if info["static"]:
            CopyDir(directory, output)
            continue

        InitDir(output, overwrite=False)

        wikiparse(directory, output)

if __name__ == "__main__":
    main()

