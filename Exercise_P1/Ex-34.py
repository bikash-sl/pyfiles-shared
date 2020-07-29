"""
34. Write a Python program to sum of two given integers. 
However, if the sum is between 15 to 20 it will return 20. 
"""


def sum(num1, num2):
    sum = num1 + num2
    if 20 > sum > 15:
        return 20
    return sum


print(sum(20, 34))

print(sum(14, 5))

input("\nPress Enter to exit ... ... ... ")
