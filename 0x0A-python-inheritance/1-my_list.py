#!/usr/bin/python3
"""
This module defines a function that inherits from list
"""


class MyList(list):
    """
    this class inherits from list
    """

    def print_sorted(self):
        """
        prints the sorted list
        """
        print(sorted(self))
