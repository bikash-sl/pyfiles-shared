"""
Exercise 7

Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list 
and makes a new list that has only the even elements of this list in it.
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("Given list is\n", a)

# One Line of code
print(f"Even list is\n{[item for item in a if item % 2 == 0]}")

# # Long format of code
# even_items = []
# for item in a:
#     if item % 2 == 0:
#         even_items.append(item)

# print(f"Even list is\n{even_items}")

input("Press Enter to exit ..... ")
