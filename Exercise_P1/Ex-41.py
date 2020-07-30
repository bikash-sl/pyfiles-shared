# 41. Write a Python program to check whether a file exists.

import os.path

with open("My_File.txt", "w") as file:
    pass

print(os.path.isfile("My_File.txt"))

input("\nPress Enter to exit ... ... ... ")
