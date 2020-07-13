# Guess the number
# the computer now tries to guess my number

# Import modules
import random

# Initializing the variables
the_number = 0
tries = 0
guess = 0
high_guess = 100
low_guess = 1

# Info about the program and input
print("\t\t\t<<<__GUESS THE NUMBER V.2__>>>\n\n")
print("The computer now tries to guess your number.")
the_number = int(input("Enter a number between 1 to 100 : "))
print("\n")

# starting the guess process
while guess != the_number:
    guess = random.randint(low_guess, high_guess)
    print(guess)
    if guess > the_number:
        print("Lower\n")
        # 1 is subtracted to avoid repetition of number
        high_guess = guess - 1
    elif guess < the_number:
        print("Higher\n")
        # 1 is added to avoid repetition of number
        low_guess = guess + 1
    tries += 1

# Showing result to the user
if guess == the_number:
    print("\nYour number was", the_number, ".")
    print("It took me only", tries, "tries.")
else:
    print("Computer is unable to guess!!!")

input("\n\nPress Enter to Exit. ")