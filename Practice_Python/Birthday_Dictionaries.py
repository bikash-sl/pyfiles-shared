"""
Exercise 33

This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: 
Part 2(Birthday Json), Part 3(Birthday Months), and Part 4(Birthday Plots).

For this exercise, we will keep track of when our friend’s birthdays are, 
and be able to find that information based on their name. 
Create a dictionary (in your file) of names and birthdays. 
When you run your program it should ask the user to enter a name, 
and return the birthday of that person back to them. 

The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
"""

import time

names_birthdays = {"Vikram Sarabhai": "12 Aug 1919",
                   "C.V. Raman": "7 Nov 1888",
                   "Mahatma Gandhi": "02 Oct 1869",
                   "Bhagat Singh": "27 Sep 1907",
                   "Vivekananda": "12 Jan 1863",
                   "Dr. B.R. Ambedkar": "14 Apr 1891",
                   "Lal Bahadur Shastri": "02 Oct 1904",
                   "A.P.J. Abdul Kalam": "15 Oct 1931"}

print("\nWelcome to the birthday dictionary. \nWe know the birthdays of: ")
time.sleep(1)

for i in names_birthdays.keys():
    print(i)

name = input("\nWho's birthday do you want to look up? ")
print(f"{name}'s birthday is {names_birthdays[name]}.")

input("\nPress Enter to exit ... ... ... ")
