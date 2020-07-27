"""
23. Write a Python program to get the n (non-negative integer) copies 
of the first 2 characters of a given string. 
Return the n copies of the whole string if the length is less than 2.
"""

string = input("Enter a string: ")

copies = int(input("How many copies do you want? "))

if len(string) > 2:
    print(copies * string[:2])
else:
    print(copies * string)


input("\nPress Enter to exit ... ... ... ")
