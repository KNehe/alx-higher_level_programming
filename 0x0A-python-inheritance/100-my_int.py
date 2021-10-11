#!/usr/bin/python3

"""
Module 100-my-int
inherits from int
has == and != inverted
"""


class MyInt(int):

    """
    implments ___eq__
    __init__ ,
    and __ne__
    """
    def __init__(self, value):
        """initialzes int"""
        self.value = value

    def __eq__(self, other):
        """equal magic method"""
        return self.value != other

    def __ne__(self, other):
        """not equal magic method"""
        return self.value == other
