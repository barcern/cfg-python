# Create a function to draw any regular shape.

import turtle as t

def draw_shape(sides, length, fill_line, fill_shape):
    """Draw a regular shape of any number of sides using turtle."""
    angle = 360 / sides
    t.begin_fill()
    for i in range(sides):
        t.color(fill_line, fill_shape)
        t.forward(length)
        t.right(angle)
    t.end_fill()

draw_shape(10, 25, 'blue', 'red')