#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry

"""

Module 8-rectangle
"""


class Rectangle(BaseGeometry):
    """
    Class that defines a rectangle from BaseGeometry Class
    """

    def __init__(self, width, height):
        """
        Initializes instance
        Args:
            width: rectangle width
            height: rectangle height
        Returns:
            Nothing.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Method that calculates the area of the rectangle
        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Method that returns the Rectangle #
        Returns:
            The string of the rectangle.
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
