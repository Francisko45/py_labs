import turtle

screen = turtle.Screen()
screen.bgcolor("white")

flag = turtle.Turtle()
flag.speed(10)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

flag.penup()
flag.goto(-150, 150)
flag.pendown()

for color in colors:
    flag.color(color)
    flag.begin_fill()
    flag.forward(450)
    flag.right(90)
    flag.forward(50)
    flag.right(90)
    flag.forward(450)
    flag.left(90)
    flag.left(90)
    flag.end_fill()

flag.hideturtle()
turtle.done()

