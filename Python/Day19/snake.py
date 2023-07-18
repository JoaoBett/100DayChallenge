from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("arrow")
        self.last_input = RIGHT

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        
    def add_segment(self, position):
        new_segment = Turtle("circle")
        new_segment.color("yellow")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
        
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.move_segment(seg_num)
        self.segments[0].forward(MOVE_DISTANCE)
        self.last_input = self.head.heading()

    def move_segment(self, seg_num):
        new_x = self.segments[seg_num - 1].xcor()
        new_y = self.segments[seg_num - 1].ycor()
        self.segments[seg_num].goto(new_x, new_y)

    def up(self):
        if self.last_input != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.last_input != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.last_input != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.last_input != RIGHT:
            self.head.setheading(LEFT)
