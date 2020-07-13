"""
Create a new canvas using the turtle module’s Pen function and
then draw a rectangle.
"""

import turtle

t = turtle.Pen()    # Canvas creation using pen

# Drawing the rectange
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

# # With loop
# for i in range(4):
#     t.forward(100)
#     t.left(90)

input("Press Enter to exit: ")
