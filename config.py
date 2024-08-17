from re import compile as ReCompile, X as ReX

OUTPUT_DIR = "build"

LINK_PATTERS = [
    (
        ReCompile(r"""\b((?:https?://|(?<!//)www\.)\w[\w_\-]*(?:\.\w[\w_\-]*)*[^<>\s"']*(?<![?!.,:*_~);])(?=[?!.,:*_~);]?(?:[<\s]|$)))""", ReX),
        r"\1"
    )
]
