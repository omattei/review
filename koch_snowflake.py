#!/usr/bin/python
#
# koch_snowflake.py: Generates a Koch snowflake to n levels and exports to an SVG image.
#
# Author:       Andrea Shaw <rshaw@olivermattei.net>
# Date Created: 31 December 2016
import sys, os
from math import sin, cos, pi, radians

import turtle
import canvasvg

" CONSTANTS "
UNIT_LENGTH = 500
BASE_THETA = 60 # degrees
" GLOBAL VARIABLES " 
screen = turtle.Screen()
screen.delay(0.0000001) # milliseconds
#screen.tracer(0, 0)

turtles = [ turtle.Turtle() for _ in range(3) ]

" SET ATTRIBUTES FOR TURTLES " 
angle = BASE_THETA 

"""
    Converts polar to rectangular coordinates with the given shift.

    @param r the radius 
    @param theta the angle
    @return a 2-tuple of x- and y-coordinates
"""
def pol2rect(r, theta, shift):
    return (
            r * cos(radians(theta) + shift),
            r * sin(radians(theta) + shift),
        ) 

for t in turtles:
    t.penup()
    t.hideturtle()
    t.goto( pol2rect(UNIT_LENGTH, angle, 15/18*pi) )
    t.seth(angle)
    
    t.pendown()
    t.speed("fastest")

    angle += 120

levels = 0

" SET NUMBER OF ITERATIONS "
if len(sys.argv) <= 3:
    try:
        levels = int(sys.argv[-1])
    except ValueError:
        pass
else: 
    exit("koch_snowflake.py: Given too many parameters!")

"""
    Draws a Koch snowflake using a 3-tuple of turtles to the given depth.

    @param turtles list of 3 turtles to draw with
    @param level the current depth drawn to
    @param length the length to draw any line segment
"""
def draw_snowflake(turtles, level, length):
    if level < 1:
        [ t.forward(length) for t in turtles ]
    else:
        draw_snowflake(turtles, level - 1, length / 3)
        [ t.left(BASE_THETA) for t in turtles ]
        draw_snowflake(turtles, level - 1, length / 3)
        [ t.right(2 * BASE_THETA) for t in turtles ]
        draw_snowflake(turtles, level - 1, length / 3)
        [ t.left(BASE_THETA) for t in turtles ]
        draw_snowflake(turtles, level - 1, length / 3)

draw_snowflake(turtles, levels, UNIT_LENGTH * 3**0.5)

filepath = os.path.join(os.getcwd(), "Koch_Snowflake_{}_Levels.svg".format(levels))
canvasvg.saveall(filepath, screen.getcanvas())

print("Saving image to", filepath, "...")

#screen.update()
screen.mainloop()
