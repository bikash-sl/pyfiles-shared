"""
Exercise 8

Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""

print("\t\t>>>>>>> Rock, Paper, Scissors || Game Running <<<<<<<\n")
print("For Rock press (R),\n"
      "For Paper press (P),\n"
      "For Scissors press (S).\n")

game_list = ["R", "P", "S"]
count = 0
usr1 = input("Enter name Player 1: ").capitalize()
score_1 = 0
tie = 0
usr2 = input("Enter name Player 2: ").capitalize()
score_2 = 0

while count < 10:

    # choice procedure
    print(f"\nChances left {10 - count}")
    choice_1 = input(f"({usr1}) Rock, Paper, Scissors: ").upper()
    choice_2 = input(f"({usr2}) Rock, Paper, Scissors: ").upper()
    if (choice_1 or choice_2) not in game_list:
        print(" !!! WRONG INPUT !!! ")
        exit()

    # game play procedure
    condition_1 = choice_1 == "P" and choice_2 == "R"
    condition_2 = choice_1 == "R" and choice_2 == "S"
    condition_3 = choice_1 == "S" and choice_2 == "P"

    if choice_1 == choice_2:
        print("Its a tie.\n")
        tie += 1
    elif condition_1 or condition_2 or condition_3:
        print(f"{usr1} got a point.\n")
        score_1 += 1
    else:
        print(f"{usr2} got a point.\n")
        score_2 += 1
    count += 1

# result declaration and stats
if score_1 > score_2:
    print(f"\t\t<<<< {usr1.upper()} WON >>>>")
elif score_1 == score_2:
    print("\t\t<<<< TIED >>>>")

print("\nStats::\n"
      f"No. of times tied {tie}.\n"
      f"No. of times {usr1} won {score_1}.\n"
      f"No. of times {usr2} won {score_2}.\n")

input("Press Enter to exit ..... ")
