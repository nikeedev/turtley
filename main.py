
from turtle import *

pensize(20)
speed(120)
hideturtle()

while True:
    times = 0
    for _ in range(100):
        left(89)
        forward(80)


    if times == 5:
        times = 0
        penup()
        goto(0, 0)
        pendown()
        clear()


    penup()
    forward(120)
    pendown()
    times += 1


