import turtle
import random

screen = turtle.Screen()
screen.setup(width = 500, height = 400)
user_guess = screen.textinput(title = "make your bet", prompt= "Which turtle will win the race? Enter a color:")
is_race_on = True
color_list = ['red', 'green', 'yellow', 'purple','orange', 'blue']
y_values = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0,6):
    new_turtle = turtle.Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color_list[turtle_index])
    new_turtle.goto(-230, y_values[turtle_index])
    all_turtles.append(new_turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_guess:
                print(f"You win.{turtle.pencolor()} has won.")
            else:
                print(f"You Lose. {turtle.pencolor()} has won")
        turtle.fd(random.randint(0,10))


screen.exitonclick()