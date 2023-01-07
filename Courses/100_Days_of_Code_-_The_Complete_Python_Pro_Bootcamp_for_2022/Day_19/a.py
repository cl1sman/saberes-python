import random
from turtle import Turtle, Screen
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtlewin the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.shape('turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + i * 40)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've won! The {wining_color} turtle is the winner!")
            else:
                print(f"You've lost! The {wining_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()