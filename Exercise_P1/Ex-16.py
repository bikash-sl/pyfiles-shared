"""
16. Write a Python program to get the difference between a given number and 17, 
if the number is greater than 17 return double the absolute difference.
"""


def diff(num):
    if num < 17:
        return abs(17 - num)

    elif num > 17:
        return (num - 17) * 2


number = int(input("Enter a number: "))

print(diff(number))

input("\nPress Enter to exit ... ... ... ")
