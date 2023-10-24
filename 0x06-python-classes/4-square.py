#!/usr/bin/python3
class Square:
    """class Square that defines a square
    Attributes:
        size (int): size of the square
    Methods:
        area: calculates the area of the square
        size: retrieves the size of the square
        size=value: sets the size of the square
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
