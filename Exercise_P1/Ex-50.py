# 50. Write a Python program to print without newline or space.

line1 = "    This is the first    line"
line2 = "This is  the   second  line    "

# following will remove white spaces from the string
# and the (end="") will continue to print in the same line
print("".join(line1.split()), end="")
print("".join(line2.split()))

input("\nPress Enter to exit ... ... ... ")
