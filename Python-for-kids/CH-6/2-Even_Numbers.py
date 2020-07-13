"""
Create a loop that prints even numbers until it reaches your year
of age or, if your age is an odd number, prints out odd numbers
until it reaches your age.
"""

age = int(input("Enter your age: "))

if (age % 2) == 0:
    for i in range(2, age+2, 2):
        print(i)
elif (age % 2) != 0:
    for i in range(1, age+2, 2):
        print(i)
