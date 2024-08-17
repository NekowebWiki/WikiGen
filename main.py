from RenderUtils import JinjaRender, RenderMarkdown
from os import listdir
from os.path import join as JoinPath
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
        "static": False
    },
    "headpages": {
        "out": "",
        "static": False
    },
    "images": {
        "out": "i",
        "static": True
    }
}

def wikiparse(input_dir: str, output: str):
    pass

def main():
    InitDir(OUTPUT_DIR)

    for directory, info in DIRECTORIES.items():
        contents = listdir(directory)
        output = JoinPath(OUTPUT_DIR, info["out"]).replace("\\", "/")

        if info["static"]:
            CopyDir(directory, output)
            continue
        
        print("Initiating " + output)

        InitDir(output, overwrite=False)

if __name__ == "__main__":
    main()

