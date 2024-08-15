from markdown2 import markdown_path as INTERNAL_MD
from jinja2 import Environment as JINJA_ENV_INIT, \
                   PackageLoader as JINJA_LOADER, select_autoescape

JinjaEnv = JINJA_ENV_INIT(
    loader=JINJA_LOADER("nekowebwiki", "views"),
    autoescape=select_autoescape()
)

WIKI_PAGE_TEMPLATE = JinjaEnv.get_template("wikipage.html")

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

