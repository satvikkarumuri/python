# draw circle with changing colors with speed 0

import turtle

# create pen
t = turtle.Pen()

# addigng bakcgrorugnd
turtle.bgcolor("black")

# set speed to zero
t.speed(0)

# input sides
sides = eval (input("how many sides do you want? "))

# rainbow colors
color = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
# start drawing 100 circles
for x in range(360):
    t.pencolor(color [x % sides])
    t.forward (x * 3 / sides + x)
    t.left(360/sides+1)
    t.width(x*sides/100)

