#!/usr/bin/python3
def safe_print_integer(value):
    """print an interger with "{:d}".format()
    Args:
        value: interger to be printed
    Returns:
        True if value is an integer
        False if value is not an integer
    Raises:
        TypeError: if value is not an integer
    """

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
