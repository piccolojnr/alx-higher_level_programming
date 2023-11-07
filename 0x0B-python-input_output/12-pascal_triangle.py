#!/usr/bin/python3
"""
    Pascal's triangle module.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n.
    Args:
        n (int): The number of rows in the triangle.
    Returns:
        A list of lists of integers representing the Pascal's triangle of n.
        If n <= 0, an empty list is returned.
        If n == 1, a list with a single 1 is returned.
        If n > 1, a list with the first n rows of Pascal's triangle is returned.
        Each row of the triangle is a list of integers representing the values
        in the row, starting with the value at the top and ending with the value
        at the bottom. The values in each row are the sum of the values in the
        row above. The first row of the triangle is always [1].
        The last row of the triangle is always [1].
        The values in each row are the sum of the values in the row above.
        The first row of the triangle is always [1].
        The last row of the triangle is always [1].
        The values in each row are the sum of the values in the row above.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
