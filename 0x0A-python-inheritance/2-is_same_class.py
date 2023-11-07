#!/usr/bin/python3

"""
module is_same_class
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class
    """
    return type(obj) == a_class
