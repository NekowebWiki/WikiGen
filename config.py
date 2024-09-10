"""
Copyright 2024 Nekoweb Wiki

This software is licensed under the 3-clause BSD license.
You should have recieved a copy of such license with this software,
if you did not, a copy can be found at the following

    https://opensource.org/license/BSD-3-Clause

Otherwise, a copy of this license can be found in the root directory
of this project.
"""

from re import compile as ReCompile, X as ReX

OUTPUT_DIR = "build"

LINK_PATTERS = [
    (
        ReCompile(r"""\b((?:https?://|(?<!//)www\.)\w[\w_\-]*(?:\.\w[\w_\-]*)*[^<>\s"']*(?<![?!.,:*_~);])(?=[?!.,:*_~);]?(?:[<\s]|$)))""", ReX),
        r"\1"
    )
]

CODE_REPOSITORY = "https://github.com/NekowebWiki/WikiGen"
SOURCE_SUFFIX = "?plain=1"
SOURCE_PREFIX = CODE_REPOSITORY + "/blob/main/"

COMMITS_PREFIX = CODE_REPOSITORY + "/commits/main/"
COMMITS_SUFFIX = ""

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
    },
    "branding": {
        "out": "",
        "static": True
    }
}

ADD_FILES = {
    "BSD-3-CLAUSE.txt": "",
    "CC_BY-SA.txt": "",
    "CNPL.txt": ""
}

COPYRIGHT_NOTICE = """Copyright 2024 Nekoweb Wiki

This software is licensed under the 3-clause BSD license.
You should have recieved a copy of such license with this software,
if you did not, a copy can be found at the following

    https://opensource.org/license/BSD-3-Clause

Otherwise, a copy of the license can be found in the root directory
of the source files, see

    https://github.com/NekowebWiki/WikiGen"""
