"""
19. Write a Python program to get a new string from a given string 
where "Is" has been added to the front. 
If the given string already begins with "Is" then return the string unchanged.
"""


def stris(string):
    if len(string) >= 2 and string[:2].upper() == "IS":
        return string
    return "Is " + string


usr_str = input("Enter a sentence or word:\n")

print("New string is:\n" + stris(usr_str))

input("\nPress Enter to exit ... ... ... ")
