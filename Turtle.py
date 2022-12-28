import random
from turtle import Turtle
from turtle import Screen
import clear


tiny_turtle=Turtle()
tiny_turtle.shape("turtle")
tiny_turtle.shapesize(.5,.5,.5)
tiny_turtle.pensize(1)
tiny_turtle.speed(15)

def change_color():
    R=random.random()
    G=random.random()
    B=random.random()
    tiny_turtle.color(R,G,B)



#PENUP AND PENDOWN
tiny_turtle.color("blue")
for i in range(4):
    tiny_turtle.rt(90)
    for x in range(10):
        tiny_turtle.pu()
        tiny_turtle.fd(10)
        tiny_turtle.pd()
        tiny_turtle.fd(10)
tiny_turtle.clear()


#SHAPES
for x in range(3,10):
    change_color()
    for i in range(x):
        tiny_turtle.rt(360/x)
        tiny_turtle.forward(100)
tiny_turtle.clear()


#RANDOM WALK
directions=[0,90,180,270]
for i in range(40):
    change_color()
    tiny_turtle.setheading(random.choice(directions))
    tiny_turtle.fd(40)
tiny_turtle.clear()


#CIRCULAR PATTERN
for i in range(72):
    change_color()
    tiny_turtle.circle(100)
    tiny_turtle.rt(5)
tiny_turtle.clear()
