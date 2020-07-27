"""
21. Write a Python program to find whether a given number (accept from the user) is even or odd, 
print out an appropriate message to the user.
"""

num = int(input("Enter a number to check whether it is even or odd: "))

if num % 2 == 0:
    print(num, "is an Even number.")
elif num % 2 != 0:
    print(num, "is an Odd number.")

input("\nPress Enter to exit ... ... ... ")
