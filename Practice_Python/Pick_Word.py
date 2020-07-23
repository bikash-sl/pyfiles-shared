"""
Exercise 30

This exercise is Part 1 of 3 of the Hangman exercise series.
The other exercises are: Part 2(Guess Letters) and Part 3(Hangman).

In this exercise, the task is to write a function that picks a random word 
from a list of words from the SOWPODS dictionary. 
Download this file(http://norvig.com/ngrams/sowpods.txt) and save it in 
the same directory as your Python code. 
This file is Peter Norvig’s compilation of the dictionary of words used in 
professional Scrabble tournaments. Each line in the file contains a single word.

Hint: use the Python random library for picking a random word.
"""

import random

with open("sowpods.txt", "r") as file:
    # creating a list of the contents in the file
    file_lst = list(file)

word = random.choice(file_lst)
print("The random word from the sowpods.txt is:", word)

input("Press Enter to exit ... ... ... ")
