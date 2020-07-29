"""
39. Write a Python program to compute the future value of a 
specified principal amount, rate of interest, and a number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
"""

p = 10000
r = 3.5
t = 7

amt = p * ((1 + (0.01 * r)) ** t)

print("The future value is:", round(amt, 2))

input("\nPress Enter to exit ... ... ... ")
