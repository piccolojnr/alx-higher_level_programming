#!/usr/bin/python3
""" Class that prevents the user from dynamically creating new instance attributes
"""


class LockedClass:
    """Prevents the user from dynamically creating new instance attributes"""

    __slots__ = ["first_name"]
