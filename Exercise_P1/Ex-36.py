# 36. Write a Python program to add two objects if both objects are an integer type.

def add_int(num1, num2):
    if type(num1) != type(num2):
        raise TypeError("Inputs must be integers.")
    return num1 + num2


print("The sum is:", add_int(2, 7))

input("\nPress Enter to exit.")
