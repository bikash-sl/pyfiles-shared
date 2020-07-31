# 55. Write a Python to find local IP addresses using Python's stdlib

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
s.close()
print("\nYour Computer IP Address is:", local_ip)

input("\nPress Enter to exit ... ... ... ")
