# Enter you module contents here
"""Here is the module docstring"""
import math

__version__ = "1.0"
__author__ = "Authored by JH"

def hypothenuse(a, b):
    """returns the length of the 
    hypothenuse when given the lengths of 
    two other sides of a right-angled 
    triangle """
    return math.sqrt(a**2 + b**2)

def area(a, b):
    """returns the area of the right-angled 
    triangle, when two sides, perpendicular 
    to each other, are given as parameters.
    """
    return a*b/2
