# Created a no. guessing game using the random module

import random

num = random.randint(1, 100)
guess_count = 0
print("There is a number hidden in this program. FIND IT.")

while guess_count < 10:

    print("\nNo. of guesses left is %s" % (10-guess_count))
    guess = int(input("Guess a number between 1 and 100: "))

    # The following block is guessing block
    if guess == num:
        print("\n\tYou guessed right !!!")
        break
    elif guess < num and guess_count != 9:
        print("Try higher")
    elif guess > num and guess_count != 9:
        print("Try lower")
    elif guess != num and guess_count == 9:
        print("\n\tGame Over !!!")

    guess_count += 1

input("\nPress Enter to exit......")
