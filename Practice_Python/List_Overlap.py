"""
Exercise 5

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements 
that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

1:  Randomly generate two lists to test this
2:  Write this in one line of Python
"""

import random

list_len = int(input("Enter the length of the list you want: "))
a = random.sample(range(1, 94), list_len)
b = random.sample(range(1, 94), list_len)
common_elements = list(set(a) & set(b))

print(f"Random lists are:\n {a}\n {b}")

if len(common_elements) > 0:
    print("\nCommon list is:\n", list(common_elements))
else:
    print("\nThere is nothing common.")

input("Press Enter to exit ..... ")
