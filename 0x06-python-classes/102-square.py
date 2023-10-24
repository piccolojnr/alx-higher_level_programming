#!/usr/bin/python3
"""defines the square class"""


class Square:
    "class of a square"

    def __init__(self, size=0):
        """Initializes the data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

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

    def area(self):
        """area: returns the area of the square"""
        return self.__size * self.__size

    def __eq__(self, __value: object) -> bool:
        """defines the == operator"""
        return self.area() == __value.area()

    def __ne__(self, __value: object) -> bool:
        """defines the != operator"""
        return self.area() != __value.area()

    def __lt__(self, __value: object) -> bool:
        """defines the < operator"""
        return self.area() < __value.area()

    def __le__(self, __value: object) -> bool:
        """defines the <= operator"""
        return self.area() <= __value.area()

    def __gt__(self, __value: object) -> bool:
        """defines the > operator"""
        return self.area() > __value.area()

    def __ge__(self, __value: object) -> bool:
        """defines the >= operator"""
        return self.area() >= __value.area()
