"""
25. Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""


def check(user_val, group):
    if user_val in group:
        return True
    return False


grp = [1, 5, 8, 3]

value = int(input("Enter an integer value of single digit: "))

print(check(value, grp))

input("\nPress Enter to exit ... ... ... ")
