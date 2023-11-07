#!/usr/bin/python3
Rectangle = __import__("9-rectangle").Rectangle

"""
    class Square that inherits from Rectangle
"""


class Square(Rectangle):
    """
    class Square that inherits from BaseGeometry
    """

    def __init__(self, size):
        """
        class Square that inherits from BaseGeometry

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Method that calculates the area of the square
        Returns:
            The area of the square.
        """
        return self.__size**2
