"""
Try using dir and help to find out how to break a string into words,
and then create a small program to print every other word in the
following string, starting with the first word ( this ):

msg = "this if is you not are a reading very this good then way you to have
hide done a it message wrong"
"""

msg = "this if is you not are a reading very this good then way you\
     to have hide done a it message wrong"

words = msg.split()

for item in words[::2]:
    print(item, end=" ")

input("\nPress Enter to exit: ")
