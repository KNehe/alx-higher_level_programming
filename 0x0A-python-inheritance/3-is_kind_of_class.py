#!/usr/bin/python3
"""
Module 3-is_kind_of_class
returns True if the object is an instance of,
or if the object is an instance of a class that
inherited from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Returns true of false"""
    return isinstance(obj, a_class)
