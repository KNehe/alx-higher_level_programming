#!/usr/bin/python3

"""
0-add_integer module
takes two values which are converted to integers
Returns sum of both
"""


def add_integer(a, b=98):
    """
    Returns sum of two integers
    """
    if type(a) not in [float, int]:
        raise TypeError("a must be an integer")
    if type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
