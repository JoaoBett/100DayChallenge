from turtle import Turtle, Screen

tim = Turtle()
tim.speed("fastest")
screen = Screen()

def move_foward():
    tim.forward(25)

def move_backwards():
    tim.backward(25)

def rotate_left():
    tim.left(25)

def rotate_right():
    tim.right(25)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_foward,"w")
screen.onkey(move_backwards,"s")
screen.onkey(rotate_left,"a")
screen.onkey(rotate_right,"d")
screen.onkey(clear,"space")
screen.exitonclick()