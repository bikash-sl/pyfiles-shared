"""
Create a function to draw an eight-sided shape like an
octagon. (Hint: Try turning the turtle 45 degrees.)
"""

import turtle

t = turtle.Pen()


def octagon(side):
    for _ in range(8):
        t.forward(side)
        t.left(45)


octagon(70)

input("Press Enter to exit......    ")
