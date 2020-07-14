"""
Exercise 3

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

1:  Instead of printing the elements one by one,
    make a new list that has all the elements less than 5 from this list in it
    and print out this new list.
2:  Write this in one line of Python.
3:  Ask the user for a number and return a list that contains only elements
    from the original list a that are smaller than that number given by the user.
"""

# The solution does not consider extra(no. 2)

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 78, 65, 69, -1, -9]
temp_list = []

for item in my_list:
    if item < 5:
        temp_list.append(item)

custom_list = []
num = int(input("Enter a number: "))

for item in my_list:
    if item < num:
        custom_list.append(item)

print("\nNumbers less than 5 are\n", str(temp_list)[1:-1])
print("\nNumbers less than %s are\n" % num, str(custom_list)[1:-1])

input("Press Enter to exit ..... ")
