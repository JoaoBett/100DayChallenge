from turtle import Turtle

STARTING_POSITION = (0,-250)
FINISH_LINE = 280
MOVE_DISTANCE = 20

class Arrow(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("arrow")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def next_level(self):
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False