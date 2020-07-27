"""
29. Write a Python program to print out a set containing all the colors from color_list_1 
which are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""

color_1 = ["White", "Black", "Red"]
color_2 = ["Red", "Green"]

color_3 = set(color_1) - set(color_2)

print(color_3)

input("\nPress Enter to exit ... ... ... ")
