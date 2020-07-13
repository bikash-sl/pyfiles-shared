my_number = 65
guess_counter = 10
user_number = int()

print("There is a number hidden in this program.",
      "\nYou have only 10 number of guesses to find it out.\n")
while guess_counter > 0:
    user_number = int(input("Enter the number: "))
    guess_counter = guess_counter - 1
    if user_number == my_number:
        print("You guessed right.", "it took only",
              str(10 - guess_counter), "attempt(s).")
        break
    elif user_number > my_number and guess_counter != 0:
        print("Please input a lesser number.\n")
    elif user_number < my_number and guess_counter != 0:
        print("Please input a greater number.\n")
    else:
        print("You are out of guesses. !!! Game Over !!!")
        break
    print("Attempt(s) left", str(guess_counter) + ".")
