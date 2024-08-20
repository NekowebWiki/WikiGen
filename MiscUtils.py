"""
Copyright 2024 Nekoweb Wiki

This software is licensed under the 3-clause BSD license.
You should have recieved a copy of such license with this software,
if you did not, a copy can be found at the following

    https://opensource.org/license/BSD-3-Clause

Otherwise, a copy of this license can be found in the root directory
of this project."""

from os.path import exists as PathExists, join as JoinPath
from shutil import rmtree as RMRF 
from os import mkdir, listdir as ls

def InitDir(directory: str, overwrite: bool = True):
    if not overwrite and PathExists(directory):
        return
    if PathExists(directory):
        RMRF(directory)
    mkdir(directory)

