"""
27. Write a Python program to 
concatenate all elements in a list into a string and return it. 
"""

lst = [1, 7, "t", "Y", "R", "a", 3, 4]


def list2str(list):
    temp_list = [str(i) for i in list]
    return "".join(temp_list)


print(list2str(lst))

input("\nPress Enter to exit ... ... ... ")
