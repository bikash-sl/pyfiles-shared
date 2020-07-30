"""
42. Write a Python program to determine 
if a Python shell is executing in 32bit or 64bit mode on OS.
"""

import struct

mode = struct.calcsize("P") * 8

print(f"You are running Python in {mode}-bit mode.")

input("\nPress Enter to exit ... ... ... ")
