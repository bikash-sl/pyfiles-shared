"""
7. Write a Python program to accept a filename from the user 
and print the extension of that.
Sample filename : abc.java
Output : java
"""

file = input("Enter the file name: ")

print("The extention of the file is: ", file.split(".")[-1])

input("\nPress Enter to exit ... ... ... ")
