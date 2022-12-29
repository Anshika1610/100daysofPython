from turtle import Turtle,Screen
import clear


tim=Turtle()

screen = Screen()

def forward():
     tim.fd(20)
def backward():
    tim.bk(20)
def anticlockwise():
    tim.lt(20)
def clockwise():
     tim.rt(20)
def clearing():
    tim.clear()

screen.listen()
screen.onkey(key="W", fun=forward)
screen.onkey(key="S", fun=backward)
screen.onkey(key="A", fun=anticlockwise)
screen.onkey(key="D", fun=clockwise)
screen.onkey(key="C", fun=clearing)

screen.exitonclick(
