# Guess my number

# Import modules
import random

# Initializing the variables
the_number = random.randint(1, 100)
tries = 0

# Info about the program
print("\t\t\t<<<__GUESS THE NUMBER__>>>\n\n")
print("I am thinking about a number between 1 to 100.")
print("Try to guess it in under 10 tries.\n")
guess = int(input("Take a guess : "))

# starting the guess process
while guess != the_number and tries < 10:
    if guess > the_number:
        print("Lower\n")
    elif guess < the_number:
        print("Higher\n")
    print("You have only", str(10 - tries), "tries left!")
    guess = int(input("Take a guess : "))
    tries += 1

# Congratulating the user
if guess == the_number:
    print("\nYou guessed it right.")
    print("It took you only", tries, "tries.")
    print("You still have", str(10 - tries), "tries to spare.")
else:
    print("\n\n\t!!!! FAILED !!!!")
    print("You have no more guesses left.")
    print("The number was", the_number, "!!!")
input("\n\nPress Enter to Exit. ")
