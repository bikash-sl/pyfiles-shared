# 52. Write a Python program to print to stderr (standard error).

import sys


def tostderr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


tostderr("Hello", "Python", sep=" - ")

input("\nPress Enter to exit ... ... ... ")
