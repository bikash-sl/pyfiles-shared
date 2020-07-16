"""
Exercise 11

Ask the user for a number and determine whether the number is prime or not.
(A prime number is a number that has no divisors except 1 and itself,
0, 1 is not a prime number.)
"""


def primality(number):
    """The Function will check primality and return True or False accordingly"""
    if number < 1 or number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


if __name__ == "__main__":
    try:
        num = int(input("Enter a number to check primality: "))
        print(primality(num))
    except ValueError:
        print(" !!! WRONG INPUT !!!")

    input("Press Enter to exit ..... ")
