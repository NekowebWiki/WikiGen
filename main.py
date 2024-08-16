from RenderUtils import JinjaRender, RenderMarkdown
from os import listdir
from CONFIG import OUTPUT_DIR

DIRECTORIES = {
    "static": {
        "out": "/",
        "static": True
    },
    "content": {
        "out": "/w",
        "static": False
    },
    "headpages": {
        "out": "/",
        "static": False
    },
    "images": {
        "out": "/i",
        "static": True
    }
}

def main():
    for directory, info in DIRECTORIES.items():
        print(f"{directory} is {'not ' if info['static'] else ''}a parsed directory")

if __name__ == "__main__":
    main()

