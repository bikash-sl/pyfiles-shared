# 43. Write a Python program to get OS name, platform and release information.

import os
import platform

print("OS Name\t\t:", os.name.capitalize())
print("OS Type\t\t:", platform.system())
print("Kernel Info\t:", platform.release())

input("\nPress Enter to exit ... ... ... ")
