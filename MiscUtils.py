"""
    This is a small static site generator written to generate the Nekoweb Wiki: <https://wiki.nekoweb.org>.
    Copyright (C) 2024  Steve0Greatness

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from os.path import exists as PathExists, join as JoinPath
from shutil import rmtree as RMRF 
from os import mkdir, listdir as ls

def InitDir(directory: str, overwrite: bool = True):
    if not overwrite and PathExists(directory):
        return
    if PathExists(directory):
        RMRF(directory)
    mkdir(directory)

