#!/usr/bin/python3
class Square:
    """class Square that defines a square
    Attributes:
        __size (int): size of the square
    Methods:
        area(): calculates the area of the square
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size**2
