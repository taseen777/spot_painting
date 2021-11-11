import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
tantan = Turtle()
tantan.speed("fastest")

colour_list = [(218, 223, 230), (230, 207, 91), (225, 149, 91),
               (122, 167, 187), (35, 110, 158), (163, 13, 22), (127, 177, 145), (233, 81, 49), (202, 67, 27),
               (192, 186, 23),
               (174, 18, 13), (33, 129, 49), (7, 99, 37), (13, 64, 39), (12, 41, 76), (242, 203, 4), (139, 79, 92),
               (88, 13, 20), (53, 166, 76), (51, 23, 19), (180, 134, 146), (6, 64, 137), (213, 68, 75), (230, 170, 161),
               (49, 151, 191), (77, 133, 186), (175, 204, 176)]
tantan.penup()
tantan.hideturtle()
tantan.setheading(225)
tantan.forward(300)
tantan.setheading(0)
no_dots = 100

for dot in range(1, no_dots + 1):
    tantan.dot(20, random.choice(colour_list))
    tantan.forward(50)

    if dot % 10 == 0:
        tantan.setheading(90)
        tantan.forward(50)
        tantan.setheading(180)
        tantan.forward(500)
        tantan.setheading(0)

screen = Screen()
screen.exitonclick()
