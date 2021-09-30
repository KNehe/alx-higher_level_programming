#!/usr/bin/python3
"""
Module 4-print_square
Prints a square with character "#"
Returns None
"""


def print_square(size):
    """
    Prints a square
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("", end="")
    else:
        print("\n".join(["#" * size for rows in range(size)]))
