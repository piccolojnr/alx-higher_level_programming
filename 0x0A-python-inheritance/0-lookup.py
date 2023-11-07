#!/usr/bin/python3

"""
    This module contains a function that returns a list of attributes and methods of an object
"""


def lookup(obj):
    """
    functions to return the list of availble attributes and methods of an object
    """
    return dir(obj)
