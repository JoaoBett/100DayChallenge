import turtle as t
import random

tim = t.Turtle()

colours = ["IndianRed","wheat"]
directions = [0,90,180,270]

for _ in range(200):
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.color(random.choice(colours))


t.done()