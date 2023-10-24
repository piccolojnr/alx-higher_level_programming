#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """Initializes the square
        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        area(): calculates the area of the square
        Returns:
            area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """gets the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
