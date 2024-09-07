"""
Copyright 2024 Nekoweb Wiki

This software is licensed under the 3-clause BSD license.
You should have recieved a copy of such license with this software,
if you did not, a copy can be found at the following

    https://opensource.org/license/BSD-3-Clause

Otherwise, a copy of the license can be found in the root directory
of the source files, see

    https://github.com/NekowebWiki/WikiGen
"""
from pygments.style import Style as PygmentsStyle
from pygments.token import Token, Comment, Keyword, Name, String, Error, Generic, Number, Operator
from pygments.formatters import HtmlFormatter
from config import COPYRIGHT_NOTICE, OUTPUT_DIR
from os.path import join as JoinPath

class WikiCode(PygmentsStyle):
    background_color = "#7b8888"

    styles = {
        Token: "",
        Comment: "#ccc",
        Keyword: "#f00",
        String: "italic #f99",
        Number: "",
        Operator: "#e9f",

        Name: "#47baff",
        Name.Attribute: "#b0e5ff",
    }

def AddSyntaxColors():
    Formatter = HtmlFormatter(
        style=WikiCode,
        cssclass="codehilite",
        linenos="inline"
    )
    CSS = "\n".join(Formatter.get_style_defs().splitlines()[5:])
    CopyingHeader = "/*\n" + COPYRIGHT_NOTICE + "\n*/\n"
    with open(JoinPath(OUTPUT_DIR, "highlight.css"), "w") as file:
        file.write(CopyingHeader+CSS)
