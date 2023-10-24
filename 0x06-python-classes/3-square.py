#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """Initializes the square

        Attributes:
            __size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        area(): calculates the area of the square
        """
        return self.__size**2
