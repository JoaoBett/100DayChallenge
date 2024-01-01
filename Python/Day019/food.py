from turtle import Turtle
import random

colors = ["blue", "yellow", "wheat", "white", "red", "green", "purple"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(colors))
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-250,250)
        random_y = random.randint(-250,250)
        self.goto(random_x, random_y)
        self.color(random.choice(colors))