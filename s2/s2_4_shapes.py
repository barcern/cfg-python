# In this exercise you'll create a program that can draw shapes with any
# number of sides. When you run the program it will ask you to input the
# number of sides that the shape should have. The program will then
# calculate the correct angle for the shape and draw it for you.

import turtle as t

sides = int(input('How many sides should your shape have? '))
angle = 360 / sides
length = 50

for i in range(sides):
    t.forward(length)
    t.right(angle)

t.done()