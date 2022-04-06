from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.title("Creating NFTs")
screen.bgcolor ("black")

timmy_the_turtle = Turtle()
timmy_the_turtle.color("blue")

for _ in range(100):
    angle = randint(10, 90)
    for pattern in range (4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

screen.exitonclick()
