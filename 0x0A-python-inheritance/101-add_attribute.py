#!/usr/bin/python3

"""
    add_attribute module
"""


def add_attribute(obj, attr_name, attr_value):
    """
    add attribute to object if possible
    :param obj: object
    :param attr_name: attribute name
    :param attr_value: attribute value
    :return: None if not possible, otherwise None.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
