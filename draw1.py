import turtle
import time

p = turtle.Pen()
p.speed(0)
p.width(5)

turtle.onscreenclick(p.setpos)

time.sleep(10)