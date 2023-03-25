from turtle import *
from random import *
dangle = (randint(10,360))

bgcolor("black")
color("green")

def move_ant_turn (angle):
    forward(50)
    right(angle)

for x in range(12):
    move_ant_turn(dangle)

done()