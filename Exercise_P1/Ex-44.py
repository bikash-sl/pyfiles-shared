# 44. Write a Python program to locate Python site-packages.

import site

print("Global site-packages paths:\n", site.getsitepackages())
print("\nUser site-packages paths:\n", site.getusersitepackages())

input("\nPress Enter to exit ... ... ... ")
