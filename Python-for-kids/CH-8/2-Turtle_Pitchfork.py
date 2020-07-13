# Creating a pitchfork

import turtle


def outer_fork(the_angle):
    t = turtle.Pen()
    t.forward(150)
    t.left(the_angle)
    t.forward(60)
    t.right(the_angle)
    t.forward(60)


def inner_fork(the_angle):
    t = turtle.Pen()
    t.forward(170)
    t.left(the_angle)
    t.forward(40)
    t.right(the_angle)
    t.forward(30)


outer_fork(90)
inner_fork(90)
outer_fork(270)
inner_fork(270)

input("Press Enter to exit: ")
