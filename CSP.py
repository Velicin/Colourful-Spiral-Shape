import turtle
import random

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
for i in range(100):
    color = random.choice(colors)
    t.pencolor(color)
    t.circle(5*i)
    t.left(10)

t.hideturtle()

turtle.done()
