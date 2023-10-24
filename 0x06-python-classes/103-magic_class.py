#!/usr/bin/python3

"""define the magic class"""
import math


class MagicClass:
    """define the magic class"""

    def __init__(self, radius=0):
        """initialize the radius"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """return the area"""
        return (self.__radius**2) * math.pi

    def circumference(self):
        """return the circumference"""
        return 2 * math.pi * self.__radius
