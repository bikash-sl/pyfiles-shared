"""
Exercise-1
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year 
that they will turn 100 years old.
"""

import datetime

now_time = datetime.datetime.now()
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"You will turn into 100 in the year {now_time.year + (100 - age)}")

input("Press Enter to exit ..... ")
