#!/usr/bin/python3
"""
Module 3-is_kind_of_class
returns True if the object is an instance of a class
that inherited (directly or indirectly) from
the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Returns true of false"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
