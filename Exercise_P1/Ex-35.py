"""
35. Write a Python program that will return true if the two given integer values are equal 
or their sum or difference is 5.
"""


def funcheck(num1, num2):
    c1 = num1 == num2
    c2 = abs(num1 - num2)
    c3 = num1 + num2

    if c1 or c2 == 5 or c3 == 5:
        return True
    return False


print(funcheck(2, 3))
print(funcheck(5, 5))
print(funcheck(8, 3))

input("\nPress Enter to exit ... ... ... ")
