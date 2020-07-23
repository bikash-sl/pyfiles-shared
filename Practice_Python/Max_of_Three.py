"""
Exercise 28

Implement a function that takes as input three variables, 
and returns the largest of the three. 
Do this without using the Python max() function!
"""
import random


def maxvalue(a, b, c):
    if (a > b) and (a > c):
        return a
    elif (b > a) and (b > c):
        return b
    elif (c > a) and (c > b):
        return c


num_1 = random.randint(1, 150)
num_2 = random.randint(0, 150)
num_3 = random.randint(10, 150)

print(num_1, num_2, num_3)


max_elem = maxvalue(num_1, num_2, num_3)

print(f"Max of three is {max_elem}.")

input("Press Enter to exit ... ... ... ")
