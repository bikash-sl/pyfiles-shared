# Coin Flip
# import modules
import random

# Initialization
event_count = 0
head_count = 0
tail_count = 0

# info
print("\t\t\t<<<__FLIP THE COIN__>>>\n\n")
print("You have a coin,")
input("press Enter to flip it 100 times. ")
print("\n")

# Coin flip simulation
while event_count < 100:

    # Assuming 1(head), 2(tail)
    coin = random.randint(1, 2)
    if coin == 1:
        head_count += 1
    elif coin == 2:
        tail_count += 1
    
    event_count += 1

# Display the no. of heads and tails
print("Number of times 'Heads' appear is", str(head_count) + ".")
print("Number of times 'Tails' appear is", str(tail_count) + ".")
