# 49. Write a Python program to list all files in a directory in Python.

import os

files = [i for i in os.listdir("/home/user")
         if os.path.isfile(os.path.join("/home/user", i))]

print(files)

input("\nPress Enter to exit ... ... ... ")
