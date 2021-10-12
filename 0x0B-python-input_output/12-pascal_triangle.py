#!/usr/bin/python3
"""
Module 12-pascal_triangle
returns a list of lists of integers
representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
     returns a list of lists of integers
     representing the Pascal’s triangle of n:
     """
    matrix = []
    if n <= 0:
        return matrix
    for line in range(1, n + 1):
        c = 1
        x = n
        y = line
        new = []
        for i in range(1, line + 1):
            # print(c, end=" ")
            new.append(c)
            c = int(c * (line - i) / i)
        matrix.append(new)
        # print(" ")
    return matrix
