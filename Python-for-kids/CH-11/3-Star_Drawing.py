"""
Create a function to draw a star that will take two parameters:
the size and number of points.
"""

import turtle

t = turtle.Pen()


def mystar(size, points):
    angle = 360 / points
    for _ in range(points+1):
        t.forward(size)
        t.left(180 - angle)
        t.forward(size)
        t.right(180 - (angle * 2))


mystar(70, 60)

input("Press Enter to exit...... ")
