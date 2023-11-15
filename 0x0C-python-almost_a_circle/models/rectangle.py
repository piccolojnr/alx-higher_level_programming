#!/usr/bin/python3
"""
    Class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Defining the Rectangle class
    Inherits from:
        Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def to_dictionary(self):
        """
        Returns a dictionary representation of this class
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

    def __str__(self) -> str:
        """
        Overwritting the str method
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__,
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height,
        )

    def update(self, *args, **kwargs):
        """
        Updates the arguments in the class
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def display(self):
        """
        Prints to stdout the representation of the rectangle
        """
        for _ in range(self.__y):
            print()
        for h in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    @property
    def width(self):
        """
        Returning private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setting private attribute
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Returning private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setting private attribute
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Returning private attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setting private attribute
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Returning private attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setting private attribute
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
