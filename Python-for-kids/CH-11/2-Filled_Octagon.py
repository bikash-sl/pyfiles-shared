# Try drawing an filled octagon with an outline

import turtle

t = turtle.Pen()


def octagon(side, filled=False):
    if filled == True:
        t.begin_fill()
    for _ in range(8):
        t.forward(side)
        t.left(45)
    if filled == True:
        t.end_fill()


octagon(60, True)

input("Press Enter to exit......    ")
