#!/usr/bin/python3
"""module that defines a function to find the peak of a list of numbers
"""


def find_peak(list_of_integers):
    """Finds the peak in a list of numbers

    Args:
        list_of_integers (_type_): list of unsorted int
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]

    for i in range(1, len(list_of_integers) - 1):
        if (
            list_of_integers[i] >= list_of_integers[i - 1]
            and list_of_integers[i] >= list_of_integers[i + 1]
        ):
            return list_of_integers[i]
