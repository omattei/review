#!/usr/bin/python
#
# koch_snowflake.py: Generates a Koch snowflake to n levels and exports to an SVG image.
#
# Author:       Andrea Shaw <rshaw@olivermattei.net>
# Date Created: 31 December 2016
import sys
import turtle
import canvasvg
import math

" CONSTANTS "
UNIT_LENGTH = 500

" GLOBAL VARIABLES " 
screen = turtle.Screen()
screen.delay(0.001) # milliseconds

turtles = [ turtle.Turtle() for _ in range(3) ]

" SET ATTRIBUTES FOR TURTLES " 
angle = 60 # degrees

def rectang(r, theta):
    return 

rectang = lambda r, theta: (r * math.cos(math.radians(theta)) + 1) 

for t in turtles:
    t.penup()

    t.goto(rectang(UNIT_LENGTH, angle))
    t.seth(angle)
    
    t.pendown()

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
    if 
