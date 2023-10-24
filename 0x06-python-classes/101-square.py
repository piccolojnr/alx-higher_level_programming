#!/usr/bin/python3
"""defines the square class"""


class Square:
    "class of a square"

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif (
            not isinstance(position, tuple)
            or len(position) != 2
            or not all(isinstance(num, int) for num in position)
            or not all(num >= 0 for num in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    @property
    def data(self):
        "gets the data"
        return self.__size

    @data.setter
    def data(self, value):
        """set data"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """gets the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area: returns the area of the square"""
        return self.__size * self.__size

    def get_print(self):
        """get_print: returns the square with the character #"""
        res = ""
        if self.__size == 0:
            res += "\n"
            return res
        for i in range(self.__position[1]):
            res += "\n"

        for i in range(self.__size):
            for j in range(self.__position[0]):
                res += " "
            for k in range(self.__size):
                res += "#"
            res += "\n"
        return res

    def my_print(self):
        """my_print: prints the square with the character #"""
        print(self.get_print(), end="")

    def __str__(self) -> str:
        """__str__: prints the square with the character #"""
        return self.get_print()
