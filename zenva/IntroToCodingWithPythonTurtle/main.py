from turtle import *

radios = [60, 20, 40, 30]
distance_planets = [100, 80, 90, 90]
colors = ["#20c99c", "#2072c9", "#a220c9", "#c9205b"]

bgcolor("black")

penup()
backward(150)
pendown()
speed(50)

for dcircle in range(4):
  begin_fill()
  color(colors[dcircle])
  circle(radios[dcircle])
  penup()
  forward(distance_planets[dcircle])
  pendown()
  end_fill()

done()