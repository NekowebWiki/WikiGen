from markdown2 import markdown_path as INTERNAL_MD

def RenderMarkdown(path: str):
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
    }
    Rendered = INTERNAL_MD(path, extras=Extras)
    return Rendered

