# Create a function that draws a triangle using turtle. (edited)

import turtle as t

def draw_triangle(length, fill_line, fill_shape):
    """Draw a triangle using turtle."""
    angle = 120
    t.begin_fill()
    for i in range(3):
        t.color(fill_line,fill_shape)
        t.forward(length)
        t.right(angle)
    t.end_fill()

draw_triangle(25,'blue','red')