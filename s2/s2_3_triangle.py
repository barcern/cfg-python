# Using turtle draw a triangle.
# A triangle has three sides and an angle of 120 degrees
# Extension 1: Make the triangle blue
# Extension 2: Draw a circle

import turtle as t

t.speed('slowest')
t.begin_fill()

for i in range(3):
    t.forward(100)
    t.right(120)

t.color('blue')
t.end_fill()

t.penup()
t.right(270)
t.forward(150)
t.pendown()
t.speed('fastest')

t.begin_fill()
for i in range(360):
    t.color('green')
    t.pensize(5)
    t.forward(50)
    t.right(1)
    t.back(50)
t.end_fill()

t.done()