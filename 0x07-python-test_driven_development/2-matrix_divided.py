#!/usr/bin/python3
""" This module contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number
    """
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row)
        for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(j / div, 2) for j in i] for i in matrix]
