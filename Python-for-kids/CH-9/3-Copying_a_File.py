"""
Create a Python program to copy a file. (Hint: You’ll need to open
the file that you want to copy, read it in, and then create a new
file—the copy.) Check that your program works by printing the
contents of the new file on the screen.
"""

import shutil

# Creats a file and writing some texts
original_file = open("Quotes.txt", "w")
original_file.write('''“A man who dares to waste one hour \
of time has not discovered the value of life.” —Charles Darwin''')
original_file.close()
print("'Quotes.txt' file created successfully.\n")

# # Novice approach of copying file contents
# # Read the Quote.txt file and copy the text to new file
# original_file = open("Quotes.txt")
# text_copied = original_file.read()
# original_file.close()

# copy_file = open("Quotes-copy.txt", "w")
# copy_file.write(text_copied)
# copy_file.close

# Using Python shutil module
shutil.copy("Quotes.txt", "Quotes-copy.txt")

# confirmation by showing o/p on screen
copy_file = open("Quotes-copy.txt")
print("\nThe following content(s) are from the 'Quotes-copy file'.")
print("\n" + copy_file.read())
copy_file.close()

input("\nPress Enter to exit......")
