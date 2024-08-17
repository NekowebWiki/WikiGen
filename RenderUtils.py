from markdown2 import markdown_path as INTERNAL_MD
from jinja2 import Environment as JINJA_ENV_INIT, \
                   FileSystemLoader as JINJA_LOADER, select_autoescape
from os import PathLike
from os.path import join as JoinPath
from config import OUTPUT_DIR
from jinja2.environment import Template as JINJA_TEMPLATE

JinjaEnv = JINJA_ENV_INIT(
    loader=JINJA_LOADER("views"),
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

def JinjaRender(
    templatein: JINJA_TEMPLATE,
    outpath: str | PathLike[str],
    **kwargs
):
    Rendered = templatein.render(**kwargs)
    with open(JoinPath(OUTPUT_DIR, outpath), "x") as f:
        f.write(Rendered)
