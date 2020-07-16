# draw circle with changing colors with speed 0

import turtle

# create pen
t = turtle.Pen()

# addigng bakcgrorugnd
turtle.bgcolor("black")

# set speed to zero
t.speed(0)

# input sides
name = turtle.textinput("enter your name ","what is your name? ")

# rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
# start drawing 100 circles
for x in range(100):
    t.pencolor(colors[ x % 4])
    t.penup()
    t.forward (x * 4)
    t.pendown()
    t.write(name, font=("Times", int(x+4/4),"bold"))
    t.left(92)

