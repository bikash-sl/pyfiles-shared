"""
33. Write a Python program to sum of three given integers. However, if two values are
equal sum will be zero.
"""

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))

sum = 0

if n1 == n2 or n3 == n1 or n2 == n3:
    sum = 0
else:
    sum = n1 + n2 + n3

print("The sum is:", sum)

input("\nPress Enter to exit ... ... ... ")
