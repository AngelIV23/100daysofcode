# from turtle import Turtle, Screen
# import turtle

# timmy = Turtle()

# print(timmy)

# timmy.shape("turtle")
# timmy.color("red", "green")
# timmy.shapesize(3,3,3)
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

my_table = PrettyTable()
my_table.add_column("Pokemon name", ["Pikachu", "Squirtel", "Bolbasaur"])
my_table.add_column("Type", ["Electric", "Water", "Fire"])
my_table.align = "l"
print(my_table)

