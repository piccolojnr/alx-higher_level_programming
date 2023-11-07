#!/usr/bin/python3
"""
    class_to_json module
"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    for JSON serialization of an object
    Args:
        obj: object to serialize
    Returns:
        dictionary description of the object
    Raises:
        None.
    """
    return obj.__dict__
