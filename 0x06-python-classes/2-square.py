#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """class Square that defines a square:"""

    def __init__(self, size=0):
        """Initializes the square

        Attributes:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
