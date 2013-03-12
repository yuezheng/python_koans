#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    sides = sorted([a, b, c])

    if sides[0] <= 0:
        raise TriangleError("No side can be zero or lower")

    if sides[0] + sides[1] <= sides[2]:
        raise TriangleError("No side be longer than the total length of the other two sides")

    if a == b == c:
        return "equilateral"

    if a == b or a == c or b == c:
        return "isosceles"

    return "scalene"


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
