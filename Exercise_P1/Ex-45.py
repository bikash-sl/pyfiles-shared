# 45. Write a python program to call an external command in Python.

from os import name
from subprocess import call

if name == "posix":
    call(["ls", "-l"])
else:
    call(["dir"])


input("\nPress Enter to exit ... ... ... ")
