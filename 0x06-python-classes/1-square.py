#!/usr/bin/python3
"""
Module 1-square
Defines a square based on module 0-square
"""


class Square:
    """Represents blueprint for a square"""

    def __init__(self, size):
        """
        Initialize the sqaure.
        Args:
            size (int): length of the square's size.
        """
        self.__size = size
