from turtle import Screen
from arrow_crossing import Arrow
from scoreboard import Scoreboard
from obstacles import Obstacles
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

arrow = Arrow()
scoreboard = Scoreboard()
obstacles = Obstacles()

screen.listen()
screen.onkey(arrow.move, "Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    obstacles.create()
    obstacles.move()

    #next level
    if arrow.finish_line():
        arrow.next_level()
        obstacles.level_up()
        scoreboard.increase_level()
        

    #detect colission with an obstacle
    for obst in obstacles.all_obstacles:
        if obst.distance(arrow) < 20:
            is_game_on = False
            scoreboard.game_over()


screen.exitonclick()
