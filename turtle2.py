# draw circle with changing colors with speed 0

import turtle

# create pen
t = turtle.Pen()

# addigng bakcgrorugnd
turtle.bgcolor("black")

# set speed to zero
t.speed(0)

# rainbow colors
color = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

# start drawing 100 circles
for x in range(100):
    # change color every iteration
    t.pencolor(color [x % 6])

    # Draw circle
    t.circle(2 * x)
    t.left(91)

