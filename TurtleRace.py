from turtle import Turtle, Screen
import random

screen=Screen()
screen.setup(width=500, height=400)

race_is_on=False

user_bet=screen.textinput(title="Place your bet.", prompt="Which turtle do you think will win this race? Choose a color: ")
colors=["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_positions=[-110, -70, -30, 10, 50, 90, 130]

all_turtles=[]

for turtle_index in range(0,7):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on=True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            winning_color=turtle.pencolor()
            if user_bet==winning_color:
                print(f"You've won! The winner is {winning_color} turtle.")
            else:
                print(f"You've lost! The winner is {winning_color} turtle.")
            race_is_on=False
        rand_distance=random.randint(1 , 10)
        turtle.fd(rand_distance)






screen.exitonclick()
