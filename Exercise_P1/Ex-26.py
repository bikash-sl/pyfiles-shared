"""
26. Write a Python program to create a histogram from a given list of integers.

e.g.:   input:  [2, 6, 9, 4]

        Output: **
                ******
                *********
                ****
"""


def histogram(list):
    for i in list:
        print(i * "*")


my_list = [2, 6, 9, 4]

histogram(my_list)

input("\nPress Enter to exit ... ... ... ")
