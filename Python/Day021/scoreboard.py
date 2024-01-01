from turtle import Turtle

POSITION = (-290,250)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(POSITION)
        self.write(f"Level : {self.level}",font=("Arial", 12,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 12,"normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()