"""
Exercise 14

Write a program (function!) that takes a list and returns a new list
that contains all the elements of the first list minus all the duplicates.

Extras:
    Write two different functions to do this
    - one using a loop and constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

my_list = [7, 1, 2, 2, 3, 11, 9, 4, 5, 6, 6, 7, 8, 9, 10, 10, 11, 5]
print("List with duplicates:\n", my_list)


# Using set
def rmdup_adv(dup_list):
    no_dup = list(set(dup_list))
    return no_dup


# Using loop
def rmdup_nov(dup_list):
    no_dup = []
    for i in dup_list:
        if i not in no_dup:
            no_dup.append(i)
    return sorted(no_dup)


print("\nList without duplicates using Set:\n", rmdup_adv(my_list))
print("\nList without duplicates using Loop:\n", rmdup_nov(my_list))

input("\nPress Enter to exit ..... ")
