#!/usr/bin/python3

"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Returning private attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setting private attribute
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the arguments in the class
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of this class
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """
        Overwritting the str method
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
