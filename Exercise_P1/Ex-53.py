# 53. Write a python program to access environment variables.

import os
import pprint


print("\n" + 80 * "#" + "\n")

print("\t\tUsers Environment Variable\n")
print(os.environ)

print(2 * ("\n" + 80 * "#" + "\n"))
print("\t\tHOME & Path Environment Variables only\n")
print("HOME:\n", os.environ["HOME"])


print("\nPath:\n", os.environ['PATH'])

input("\nPress Enter to exit ... ... ... ")
