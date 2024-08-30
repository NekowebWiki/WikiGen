"""
Copyright 2024 Nekoweb Wiki

This software is licensed under the 3-clause BSD license.
You should have recieved a copy of such license with this software,
if you did not, a copy can be found at the following

    https://opensource.org/license/BSD-3-Clause

Otherwise, a copy of this license can be found in the root directory
of this project."""

from os.path import exists as PathExists, join as JoinPath, isdir
from shutil import rmtree as RMRF, copy as CopyFile
from os import mkdir, listdir as ls
from distutils.dir_util import copy_tree as CopyDir

def InitDir(directory: str, overwrite: bool = True):
    if not overwrite and PathExists(directory):
        return
    if PathExists(directory):
        RMRF(directory)
    mkdir(directory)

def GenericCopy(path: str, output: str):
    InitDir(output, overwrite=False)
    if not PathExists(path):
        return
    if isdir(path):
        CopyDir(path, output)
    CopyFile(path, output)

def IncludeExclude(directory: str) -> tuple[dict[str, list[str]|bool]]:
    BUILD_INCLUDE_PATH = JoinPath(directory, ".buildinclude")
    BUILD_EXCLUDE_PATH = JoinPath(directory, ".buildexclude")
    build_include = {
        "included": [],
        "enabled": False
    }
    build_exclude = {
        "included": [],
        "enabled": False
    }

    if PathExists(BUILD_INCLUDE_PATH):
        with open(BUILD_INCLUDE_PATH) as BUILD_INCLUDE:
            build_include["included"] = [
                JoinPath(directory, path)
                for path
                in BUILD_INCLUDE.read().splitlines()
            ]
            build_include["enabled"]  = True
    if PathExists(BUILD_EXCLUDE_PATH):
        with open(BUILD_EXCLUDE_PATH) as BUILD_EXCLUDE:
            build_exclude["included"] = [
                JoinPath(directory, path)
                for path
                in BUILD_EXCLUDE.read().splitlines()
            ]
            build_exclude["enabled"]  = True

    return build_include, build_exclude

def IncludeExcludeTest(include: dict[str, list[str]|bool], exclude: dict[str, list[str]|bool], path: str) -> bool:
    IsIncluded = (
            include["enabled"] and
            path not in include["included"]
        ) # File wasn't included
    IsExcluded = (
            exclude["enabled"] and
            path in exclude["included"]
        ) # File excluded
    return IsIncluded or IsExcluded # Returns False if both passed, or True if not

