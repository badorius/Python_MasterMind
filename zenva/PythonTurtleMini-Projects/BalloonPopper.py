from turtle import *
from random import *

diameter = 40
pop_diameter = 100
colors = ["red", "blue", "yellow", "green", "red", "black"]
bgcolor("black")


def change_color():
    color(colors[randint(0, 6)])


def draw_ballon():
    dot(diameter)


def inflate_ballon ():
    global diameter
    diameter = diameter + 10
    draw_ballon()

    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write("POP!")
        change_color()


change_color()
draw_ballon()
onkey(inflate_ballon, "Up")
listen()
done()