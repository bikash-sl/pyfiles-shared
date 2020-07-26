"""
18. Write a Python program to calculate the sum of three given numbers, 
if the values are equal then return three times of their sum.
"""


def sum(n1, n2, n3):
    sum = n1 + n2 + n3

    if n1 == n2 == n3:
        sum = sum * 3
    return sum


n = input("Enter three numbers (separate by comma) to find their sum: ")

nums = [int(i) for i in n.split(",")]

print("The sum is: ", sum(nums[0], nums[1], nums[2]))

input("\nPress Enter to exit ... ... ... ")
