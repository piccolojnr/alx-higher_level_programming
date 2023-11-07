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
