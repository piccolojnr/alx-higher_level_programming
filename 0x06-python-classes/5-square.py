#!/usr/bin/python3
"""
This module defines a Square class
"""


class Square:
    """class square that defines a square by:"""

    def __init__(self, size=0):
        """Initializes the attributes

        Attributes:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """gets the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size
        Args:
            value (int): size of the square
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        Returns:
            None
        Sets the size of the square
        to the value passed in the parameter
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area: calculates the area of the square"""
        return self.__size**2

    def my_print(self):
        """my_print: prints the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
