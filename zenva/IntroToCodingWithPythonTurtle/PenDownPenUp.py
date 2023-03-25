from turtle import *

radios = [100, 75, 50, 25]
colors = ["#20c99c", "#2072c9", "#a220c9", "#c9205b"]

bgcolor("black")

for dcircle in range(4):
  begin_fill()
  color(colors[dcircle])
  circle(radios[dcircle])
  penup()
  forward(10 + radios[dcircle])
  pendown()
  end_fill()