#!/usr/bin/python3

"""
    BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """
        Raises an exception
        """
        raise Exception("area() is not implemented")


bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
