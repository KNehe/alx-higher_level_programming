#!/usr/bin/python3

"""
Module 1-rectangle
Defines a rectangle
Basic empty class
"""


class Rectangle:
    """
    Defines a rectangle
    Private attributes width and height
    """
    def __init__(self, width=0, height=0):
        """ Initialize width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Accesses the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Mutates the width
        Args:
            value (int): new width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Accesses the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Mutates the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
