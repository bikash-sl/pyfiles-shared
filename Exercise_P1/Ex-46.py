# 46. Write a python program to get the path and name of the file that is currently executing.

import os

print("Current file path an name: ", os.path.realpath(__file__))

input("\n press Enter to exit ... ... ... ")
