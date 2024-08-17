from os.path import exists as PathExists, join as JoinPath
from shutil import rmtree as RMRF 
from os import mkdir, listdir as ls

def InitDir(directory: str, overwrite: bool = True):
    if not overwrite and PathExists(directory):
        return
    if PathExists(directory):
        RMRF(directory)
    mkdir(directory)

