#!/usr/bin/python3
"""
Module 2-square
Defines a square based on module 1-square
"""


class Square:
    """Represents blueprint for a square"""

    def __init__(self, size=0):
        """
        Initialize the sqaure.
        Args:
            size (int): length of the square's size.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
