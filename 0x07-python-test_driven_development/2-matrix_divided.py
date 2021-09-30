#!/usr/bin/python3

"""
Module 2-matrix_divided
Divides all elements of a matrix
Return divided matrix
"""


def matrix_divided(matrix, div):
    """
    Returns divided matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    msg2 = "Each row of the matrix must have the same size"

    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg2)

    new_matrix = []
    length = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(msg1)
        if len(lists) != length:
            raise TypeError(msg2)
        newlist = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(msg1)
            newlist.append(round(i/div, 2))
        new_matrix.append(newlist)
    return new_matrix
