"""
51. Write a Python program to determine profiling of Python programs.
Note: A profile is a set of statistics that describes how often and 
for how long various parts of the program executed. 
These statistics can be formatted into reports via the pstats module.
"""

import profile
import pstats


def pretest():
    for _ in range(1000):
        pass


def test():
    for _ in range(10000):
        pretest()
        pass


pf = profile.Profile()
pf.run("test()")
stats = pstats.Stats(pf)

stats.sort_stats("time", "name").print_stats()

input("\nPress Enter to exit ... ... ... ")
