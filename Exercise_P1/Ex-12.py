"""
12. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module. 
"""

import calendar

year = int(input("Enter the Year: "))
month = int(input(f"Enter the month in (mm): "))

print("\n" + calendar.month(year, month))


input("\nPress Enter to exit ... ... ... ")
