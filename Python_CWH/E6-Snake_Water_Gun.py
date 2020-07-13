"""
Snake water gun (~ stone, paper, Scissor)
Create a snake water gun game in Python!
Search Snake water gun game in google if you need help on rules
and how to play the game!
The game is to be played for 10 times (use while loop)
Display result
"""

import random

print("\t\t>>>>>>> Snake, Water, Gun || Game Running <<<<<<<\n")
print("For Snake press (S),\n"
      "For Water press (W),\n"
      "For Gun press (G).\n")

game_list = ["S", "W", "G"]
count = 0
player_score = 0
tie = 0
cpu_score = 0

while count < 10:

    # choice procedure
    print(f"Chances left {10 - count}")
    cpu_choice = random.choice(game_list)
    player_choice = input("Snake, Water, Gun: ").upper()
    if player_choice not in game_list:
        print(" !!! WRONG INPUT !!! ")
        exit()

    # game play procedure
    condition_1 = player_choice == "S" and cpu_choice == "W"
    condition_2 = player_choice == "G" and cpu_choice == "S"
    condition_3 = player_choice == "W" and cpu_choice == "G"
    
    if player_choice == cpu_choice:
        print("Its a tie.\n")
        tie += 1
    elif condition_1 or condition_2 or condition_3:
        print("You got 1 point.\n")
        player_score += 1
    else:
        print("CPU got 1 point.\n")
        cpu_score += 1
    count += 1

# result declaration and stats
if cpu_score < player_score:
    print("\t\t<<<< YOU WON >>>>")
elif cpu_score > player_score:
    print("\t\t<<<< YOU LOSE >>>>")
else:
    print("\t\t<<<< TIED >>>>")

print("\nStats::\n"
      f"No. of times tied {tie}.\n"
      f"No. of times You won {player_score}.\n"
      f"No. of times CPU won {cpu_score}.\n")