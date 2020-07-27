# 24. Write a Python program to test whether a passed letter is a vowel or not.

vowels = ["a", "e", "i", "o", "u"]

letter = input("Enter the english alphabet: ")

if letter.lower() in vowels:
    print("It is a vowel.")
else:
    print("It is a consonant.")

input("\nPress Enter to exit ... ... ... ")
