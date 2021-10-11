#!/usr/bin/python3
"""
Module 2-is_same_class.py
returns True if the object is exactly
an instance of the specified class;
otherwise False.
"""


def is_same_class(obj, a_class):
    """Returns true of false"""
    return type(obj) == a_class
