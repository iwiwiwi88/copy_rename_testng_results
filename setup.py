# -*- coding: utf-8 -*-
import os, sys
from cx_Freeze import setup, Executable

pythonExePath = os.path.split(sys.executable)
pythonFolder=pythonExePath[0]+'\\'
os.environ['TCL_LIBRARY'] = pythonFolder+'tcl\\tcl8.6'
os.environ['TK_LIBRARY'] = pythonFolder+'tcl\\tk8.6'
includes      = []
include_files = [pythonFolder+'DLLs\\tcl86t.dll', \
                 pythonFolder+'DLLs\\tk86t.dll']

setup(
      name = "CopyTestResults",
      version = "1.0",
      description = "Automation results copy and rename",
      options = {"build_exe": {"includes": includes, "include_files": include_files}},
      executables = [Executable("copy_test_results.py", base = "Win32GUI")])