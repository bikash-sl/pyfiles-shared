"""
Add functions to the Giraffes class to move the giraffe’s left and
right feet forward and back.
Then create a function called dance to teach Reginald to dance
(the function will call the four foot functions you’ve just created).
"""


class things:
    pass


class inanimate(things):
    pass


class sidewalks(inanimate):
    pass


class animates(things):
    pass


class animals(animates):
    def breathe(self):
        print('breathing')

    def move(self):
        print('Moving')

    def eat_food(self):
        print("Eating food")


class mammals(animals):
    def feed_young_with_milk(self):
        print("Feeding young")


class giraffes(mammals):
    def eat_leaves(self):
        print("Eating leaves from tree")

    def find_food(self):
        self.move()
        print("I've found some food !!")
        self.eat_food()

    def dance_a_jig(self):
        for _ in range(5):  # '_' is used to avoid the err: Unused varriable
            self.move()

    def __init__(self, spots=120):
        self.giraffe_spots = spots

    def left_foot_fwd(self):
        print("Left foot forward")

    def right_foot_fwd(self):
        print("Right foot forward")

    def left_foot_rev(self):
        print("Left foot back")

    def right_foot_rev(self):
        print("Right foot back")

    def dance(self):
        self.left_foot_fwd()
        self.left_foot_rev()
        self.right_foot_fwd()
        self.right_foot_rev()
        self.left_foot_rev()
        self.right_foot_rev()
        self.right_foot_fwd()
        self.left_foot_fwd()


reginald = giraffes()

reginald.dance()
