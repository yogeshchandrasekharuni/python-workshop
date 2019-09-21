
#Design Hexagon

from turtle import *

pencolor('blue')

colors = ["blue", "green", "orange", "red", "yellow", "purple"]

for i in range(360):
    pencolor(colors[i%6])
    width(i/100 + 1)
    forward(i)
    left(59)
    
