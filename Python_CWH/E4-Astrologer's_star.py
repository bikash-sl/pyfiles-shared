"""
Take a number from the user and print the number of star in decreasing(For true)
or increasing(For false) order.
For True or False input take user input in the form of 1 or 0.
"""

print("\t"*5, "*** Star Pattern Printing ***\n")
star_number = int(input("Enter the number of Stars: "))
print_order = int(input("Choose between 1 (increasing order) or 0 (decreasing order): "))

# My Solution
if print_order == 0:
    for star in range(star_number):
        print(star_number * "*")
        star_number = star_number - 1
elif print_order == 1:
    rev_star_number = 1
    while rev_star_number <= star_number:
        print(rev_star_number * "*")
        rev_star_number += 1
else:
    print("The sky is full of clouds.")

# Video Solution
# if print_order == 1:
#     for star in range(star_number, 0, -1):
#         print(star * "*")
# elif print_order == 0:
#     for star in range(0, star_number+1):
#         print(star * "*")
# else:
#     print("The sky is full of clouds no stars visible.")
