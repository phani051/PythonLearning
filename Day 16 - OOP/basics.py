# import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
#
# my_screen = Screen()
# turtle.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
#table.field_names = ["Pokemon Name", "Type"]
# table.add_rows(
#     [
#         ["Pikachu", "Electric"],
#         ["Squirtel", "Water"],
#         ['Charmender', 'Fire']
#     ]
# )
table.add_column("Pokemon Name", ["Pikachu", "Squirtel", "Chanrmender"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
