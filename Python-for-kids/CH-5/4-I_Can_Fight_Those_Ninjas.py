"""
Create an if statement that prints the string “That’s too many”
if the variable ninjas contains a number that’s less than 50, prints
“It’ll be a struggle, but I can take ’em” if it’s less than 30, and
prints “I can fight those ninjas!” if it’s less than 10. You might
try out your code with:
ninjas = 5
"""

ninjas = 5

if ninjas >= 0 and ninjas <= 10:
    print("Yes, I can fight those ninjas.")
elif ninjas >= 10 and ninjas <= 30:
    print("It’ll be a struggle, but I can take ’em.")
elif ninjas >= 30 and ninjas <= 50:
    print("That’s too many.")
else:
    print("I need backup.")
