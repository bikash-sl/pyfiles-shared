"""
40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)                  [Pythagoras theorem]
"""

import math


def distance(x1, y1, x2, y2):
    p_sqr = math.pow(x2 - x1, 2)
    b_sqr = math.pow(y2 - y1, 2)
    dist = math.sqrt(p_sqr + b_sqr)
    return dist


x_1 = int(input("Enter the value of x1: "))
y_1 = int(input("Enter the value of y1: "))
x_2 = int(input("Enter the value of x2: "))
y_2 = int(input("Enter the value of y2: "))

print(f"The distance between ({x_1}, {y_1}) and ({x_2}, {y_2}) is:", end=" ")
print(distance(x_1, y_1, x_2, y_2))

input("\nPress Enter to exit ... ... ... ")
