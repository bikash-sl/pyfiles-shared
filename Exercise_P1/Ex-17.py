"""
17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""


def nearest(num):
    nearest_1 = abs(1000 - num)
    nearest_2 = abs(2000 - num)

    if (nearest_1 or nearest_2) <= 100:
        return True
    return False


n = int(input("Enter a number to check whether it is nearest to 1000 or 2000: "))

print(nearest(n))

input("\nPress Enter to exit ... ... ... ")
