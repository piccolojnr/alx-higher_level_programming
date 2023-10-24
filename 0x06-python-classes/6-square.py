#!/usr/bin/python3
"""Defines a square"""


class Square:
    """class square that defines a square by:"""

    def __init__(self, size=0, position=(0, 0)):
        """Attributes:
        size (int): size of the square
        position (tuple): position of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """size: returns the size of the square"""
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

    @property
    def position(self):
        """returns the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of the square
        to the value passed in the parameter
        Args:
            value (tuple): position of the square
        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        Returns:
            None
        Sets the position of the square
        to the value passed in the parameter
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """area: returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """my_print: prints the square with the character #"""
        if self.__size == 0:
            print()
            return
        [print("") for i in range(self.__position[1])]

        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
