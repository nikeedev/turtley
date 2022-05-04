import random
from turtle import *

pensize(20)
speed(120)
hideturtle()

while True:
    times = 0
    for _ in range(100):
        left(random.randint(46, 89))
        forward(80)


    if times == 5:
        times = 0
        clear()
        penup()
        goto(0, 0)
        pendown()


    penup()
    forward(120)
    pendown()
    times += 1


