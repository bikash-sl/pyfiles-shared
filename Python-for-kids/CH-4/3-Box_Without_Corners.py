import turtle

t = turtle.Pen()

# Drawing a square without corners
for i in range(4):
    t.forward(100)
    t.up()
    t.left(45)
    t.forward(30)
    t.down()
    t.left(45)

input("Press Enter to exit: ")
