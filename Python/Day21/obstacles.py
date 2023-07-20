from turtle import Turtle
import random

COLORS = ["red", "orange", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Obstacles:

    def __init__(self):
        self.all_obstacles = []
        self.obstacle_speed = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_obstacle = Turtle("square")
            new_obstacle.shapesize(stretch_wid=2, stretch_len=1)
            new_obstacle.penup()
            new_obstacle.color(random.choice(COLORS))
            random_y = random.randint(-280,280)
            new_obstacle.goto(300, random_y)
            self.all_obstacles.append(new_obstacle)

    def move(self):
        for obst in self.all_obstacles:
            obst.backward(self.obstacle_speed)

    def level_up(self):
        self.obstacle_speed += MOVE_INCREMENT