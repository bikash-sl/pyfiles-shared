"""
Creating a program that will take user weight ang weight to be gained each year
and the number of times the user will visit the moon. 
Then calculating the weight in the moon during each visit.
Given weight in the moon is 16.5% of the earth.
"""

import sys


def basic_moon_weight():

    print("Enter your weight on earth: ")
    weight = float(sys.stdin.readline())

    print("Enter the weight you may gain each year: ")
    gain = float(sys.stdin.readline())

    print("How many years do you want to visit moon? :  ")
    no_of_yrs = int(sys.stdin.readline())

    for year in range(1, (no_of_yrs + 1)):
        moon_wt = weight * 0.165
        weight += gain
        print("Year %s your weight in the moon is %s" % (year, moon_wt))


basic_moon_weight()
