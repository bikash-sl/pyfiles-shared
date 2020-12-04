"""
3. Find double space within a string.
4. Replace double space with single space.
"""

my_str = "He is  a good boy."

# Detecting double space
spaces = my_str.find("  ")

print("Double space at position", spaces)

# Replacing double space with single space
my_str = my_str.replace("  ", " ")

print("After replacing the double space with single space\n" + my_str)
