"""
Exercise 2

Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

1:  If the number is a multiple of 4, print out a different message.
2:  Ask the user for two numbers: one number to check (call it num) 
    and one number to divide by (check). If check divides evenly into num,
    tell that to the user.
    If not, print a different appropriate message.
"""

# Ex-2
num = int(input("Enter your number: "))
check = int(input("Enter the number to check divisibility: "))

if num % 2 == 0:
    print(f"{num} is Even.")
    if num % 4 == 0:
        print(f"It is also a multiple of 4.")
elif num % 2 != 0:
    print(f"{num} is Odd.")

if num % check == 0:
    print(f"It is divisible by {check}.")
if num % check != 0:
    print(f"It is not divisible by {check}.")

input("Press Enter to exit ..... ")
