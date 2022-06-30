import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(10):
    for colours in ["red", "magenta", "blue","cyan","green","yellow","white"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.lt(10)

turtle.hideturtle()
