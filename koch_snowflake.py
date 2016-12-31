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


