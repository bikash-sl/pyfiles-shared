"""
Exercise 16

Write a password generator in Python.
Be creative with how you generate passwords -
strong passwords have a mix of
    (lowercase letters, uppercase letters, numbers, and symbols.)
The passwords should be random,
generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:
    Ask the user how strong they want their password to be.
    For weak passwords, pick a word or two from a list.
"""

import string
import random


def compulsory():
    """returns the compulsory elements for a password as a list.
    i.e. One Uppercase, lowercase, digit, special character, from each."""
    basic = [random.choice(string.ascii_lowercase),
             random.choice(string.ascii_uppercase),
             random.choice(string.digits),
             random.choice(string.punctuation)]
    random.shuffle(basic)
    return basic


def genpw(length=8, characters=string.punctuation
          + string.ascii_letters+string.digits):
    """Generates a random password of default length 8 characters (w/o repetition),\
        from the elements in characters(alpha-numeric-special) parameter.
    \nThe maximum length is 'len(characters)'."""

    if 8 <= length < len(characters):
        basic_elm = compulsory()
        more_elm = random.sample(
            list(set(characters) - set(basic_elm)),
            length - len(basic_elm))
        password = basic_elm + more_elm
        return "".join(password)


if __name__ == "__main__":

    import time

    def closing():
        print("\nClosing Wait ...")
        for i in range(3):
            time.sleep(1)
            print((i+1) * "...")

    pwd = ""
    title = "Password Generator"

    print(4*"\t", len(title)*"*", "\n",
          4*"\t", title, "\n",
          4*"\t", len(title)*"*")

    while True:
        print("Choose the type of password\n"
              "For Weak - W\n"
              "For Strong - S\n"
              "For Very strong - V")

        pw_choice = input("\nEnter here: ").upper()
        if pw_choice not in ("W", "S", "V"):
            print("!!! Wrong Input !!!\n")
            continue

        # Generating a weak password of length (4 to 7) characters
        if pw_choice == "W":
            scope = random.randint(4, 7)
            weak_lst = ['r', '@', '-', '_', 'J', '4', '0', 'M', 'x', "&"]
            pw_lst = compulsory() + random.sample(weak_lst, (scope-4))
            pwd = "".join(pw_lst)

        # Generating a strong password of length (8 to 11) characters
        elif pw_choice == "S":
            pwd = genpw(random.randint(8, 11))

        # Generating a very strong password of length (12 to 16) characters
        elif pw_choice == "V":
            pwd = genpw(random.randint(12, 16))

        print(f"Your Password is: {pwd}")

        carry_on = input("\nDo you want another password (Y/N): ").upper()
        if carry_on == "Y":
            continue

        closing()
        break
