# Using the turtle module, write a program to draw a house. The house should
# have a roof, a door and some windows at least.

# Import turtle module
import turtle as t

t.speed('fastest')

# Write a function to draw any regular shape
def draw_shape(sides, length):
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.right(angle)

# Write a function to draw a window
def draw_window():
    t.begin_fill()
    t.color('black', '#53DBFF')
    draw_shape(4, 60)
    t.end_fill()
    t.forward(30)
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(60)

# Draw an outline of the roof
t.begin_fill()
t.color('red', 'red')
draw_shape(3,-200)
t.end_fill()

# Transport pen
t.penup()
t.right(180)
t.forward(200)
t.pendown()

# Draw the house
t.begin_fill()
t.color('black', 'orange')
draw_shape(4,-200)
t.end_fill()

# Transport pen
t.penup()
t.right(180)
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(20)
t.pendown()

# Draw a door
t.begin_fill()
t.color('black', 'yellow')
t.right(90)
t.forward(50)

# Door handle
t.right(90)
t.forward(10)
t.backward(10)
t.left(90)

# Back to door
t.forward(50)
t.right(90)
t.forward(40)
t.right(90)
t.forward(100)
t.end_fill()

# Transport pen
t.penup()
t.right(90)
t.forward(70)
t.right(90)
t.forward(120)
t.right(90)
t.forward(30)
t.right(180)
t.pendown()

# Draw window 1
draw_window()

# Transport pen
t.penup()
t.right(90)
t.forward(30)
t.left(90)
t.forward(40)
t.left(90)
t.pendown()

# Draw window 2
draw_window()

# Transport pen
t.penup()
t.forward(120)
t.right(90)
t.backward(50)
t.pendown()

# Draw some greenery
t.begin_fill()
t.color('green', 'green')
draw_shape(3, 15)
t.forward(15)
draw_shape(3, 18)
t.forward(15)
draw_shape(3,10)
t.forward(10)
draw_shape(3,25)
t.forward(25)
draw_shape(3,15)
t.forward(60)
draw_shape(3,23)
t.forward(15)
draw_shape(3,19)
t.forward(19)
draw_shape(3,14)
t.forward(14)
draw_shape(3,28)
t.end_fill()

# Transport pen
t.penup()
t.goto(-150,60)
t.pendown()

# Draw a chimney
t.begin_fill()
t.color('black', 'black')
t.forward(10)
t.right(90)
t.forward(50)
t.right(90)
t.forward(10)
t.right(90)
t.forward(50)
t.end_fill()

# Transport pen
t.penup()
t.goto(-175, 135)
t.pendown()

# Draw smoke
t.begin_fill()
t.color('grey', 'grey')
t.circle(20)
t.penup()
t.goto(-195, 180)
t.pendown()
t.circle(30)
t.end_fill()

# Complete the drawing
t.done()
