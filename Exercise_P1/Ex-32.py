"""
32. Write a Python program to get the least common multiple (LCM) of two positive
integers.
"""

import math


def lcm(num1, num2):
    """Calculate LCM of two integer value."""
    lcm_of_2 = (num1 * num2) / math.gcd(num1, num2)
    return lcm_of_2


if __name__ == "__main__":

    num_1 = int(input("Enter a positive integers: "))
    num_2 = int(input("Enter another positive integers: "))

    print("The least common multiple is:", int(lcm(num_1, num_2)))

    input("\nPress Enter to exit ... ... ... ")
