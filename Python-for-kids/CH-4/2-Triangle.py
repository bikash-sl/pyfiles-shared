"""
Create another canvas, and this time, draw a triangle. Look back
at the diagram of the circle with the degrees (“Moving the Turtle”
on page 46) to remind yourself which direction to turn the turtle
using degrees.
"""

import turtle

t = turtle.Pen()    # Canvas created

# Draw a triangle
for i in range(3):
    t.forward(100)
    t.left(120)

input("Press Enter to exit: ")
