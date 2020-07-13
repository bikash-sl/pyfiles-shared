# Fortune cookie program

# Import the module
import random

# initialize the variables
fortune_1 = "fortune 1 text"
fortune_2 = "fortune 2 text"
fortune_3 = "fortune 3 text"
fortune_4 = "fortune 4 text"
fortune_5 = "fortune 5 text"

# Give instruction to the user
print("\t\t\t<<<__FORTUNE COOKIE__>>>\n\n")
print("You have five fortune cookies.")
input("\nPress 'Enter' to choose one ")

# Fortune cookie simulation
fortune = random.randint(1, 5)
if fortune == 1:
    print(fortune_1)
elif fortune == 2:
    print(fortune_2)
elif fortune == 3:
    print(fortune_3)
elif fortune == 4:
    print(fortune_4)
elif fortune == 5:
    print(fortune_5)
else:
    print("\"Better Luck Next Time\"")

# Wait for user to exit
input("\n\nPress Enter to Exit ")
