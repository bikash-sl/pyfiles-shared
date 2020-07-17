"""
Exercise 18

Create a program that will play the “cows and bulls” game with the user.
The game works like this:
Randomly generate a 4-digit number.
Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.
” Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game!
  Enter a number:
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...

Until the user guesses the number.
"""

import random


def cowbull(num, guess):
    """The function take two parameters a number and a guessed number
    and compare to return values (cows, bulls)."""

    # convert digits in the number into list
    num_list = [int(i) for i in str(num)]
    guess_list = [int(x) for x in str(guess)]
    cow, bull = 0, 0

    # comparing values in num_list and guess_list.
    for i in guess_list:
        if i in num_list:
            cow += 1
        bull = 4 - cow
    return cow, bull


if __name__ == "__main__":

    print("\t\tWelcome to the Cows and Bulls Game!\n")

    num_gen = str(random.randint(1000, 10000))
    cow_total = 0
    bull_total = 0
    count = 0

    while True:
        count += 1
        guess_num = (input("Enter [Q] to Quit... \n\tOR\n"
                           f"Guess the {len(num_gen)} digit number: "))

        if guess_num.upper() == "Q":
            quit()
        elif len(num_gen) != len(guess_num):
            print("Only four-digit number allowed.\n")
            continue

        # Gameplay
        cows, bulls = cowbull(num_gen, guess_num)
        cow_total += cows
        bull_total += bulls
        print(f"{cows} Cow(s), {bulls} Bull(s).\n")
        if guess_num == num_gen:
            print(f"You guessed in {count} attempt(s).")
            print(f"Total: {cow_total} Cow(s), {bull_total} Bull(s).")
            input("Press Enter to exit ..... ")
            break
