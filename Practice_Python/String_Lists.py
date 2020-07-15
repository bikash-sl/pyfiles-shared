"""
Exercise 6

Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
e.g.: madam, racecar, nurses run
"""


def palindrome(string):
    new_string = string.replace(" ", "")
    reverse_word = "".join(reversed(new_string))
    if reverse_word.lower() == new_string.lower():
        return True
    else:
        return False


if __name__ == "__main__":
    usr_word = input("Enter the word or sentence to check Palindrome:\n")
    print(palindrome(usr_word))
