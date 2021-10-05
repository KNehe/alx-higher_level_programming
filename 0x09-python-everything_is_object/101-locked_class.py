#!/usr/bin/python3
"""
Module 101-locked_class.py
Contains lockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name
"""


class LockedClass(object):
    """
    slots for empty locked class
    """

    __slots__ = ["first_name"]
