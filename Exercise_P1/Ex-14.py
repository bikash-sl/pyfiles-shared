"""
14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

from datetime import date

dt_1 = date(2014, 7, 2)
dt_2 = date(2014, 7, 11)

diff = dt_2 - dt_1

print(f"Difference between {dt_1} and {dt_2} is: {diff.days} days.")

input("\nPress Enter to exit ... ... ... ")
