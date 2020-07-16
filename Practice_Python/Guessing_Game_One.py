"""
Exercise 9

Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:
    Keep the game going until the user types “exit”
    Keep track of how many guesses the user has taken,
    and when the game ends, print this out.
"""

import random

while True:
    gen_num = random.randint(1, 10)
    attempts = 0
    print("\nThere is a hidden number in between 1 to 9.")

    while True:
        attempts += 1
        try:
            guess = int(input("\nGuess the number: "))
            if gen_num == guess:
                print(f"\nYou guessed right in {attempts} attempt(s).")
                break
            elif gen_num < guess:
                print("Try little low.")
            elif gen_num > guess:
                print("Try little high.")
        except ValueError:
            print(" !!! WRONG INPUT !!!\n")
            break

    try:
        cont = input("Do you want to play more (Y/N): ")
        if cont.upper() == "N":
            break
    except ValueError:
        print(" !!! WRONG INPUT !!!\n")
        break
