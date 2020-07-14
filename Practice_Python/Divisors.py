"""
Exercise 4

Create a program that asks the user for a number and
then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is,
it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

num = int(input("Enter a number: "))
divisor_list = []

for i in range(1, num+1):
    if num % i == 0:
        divisor_list.append(i)

print("Divisor(s) of %s is(are)\n" % num, str(divisor_list)[1:-1])

input("Press Enter to exit .....")
