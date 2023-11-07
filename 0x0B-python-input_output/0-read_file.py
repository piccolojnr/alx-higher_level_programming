#!/usr/bin/python3

"""
    Read a file and print its contents
"""


def read_file(filename=""):
    """
    print the contents of a file
    :param filename: the name of the file to read
    :return: nothing
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
