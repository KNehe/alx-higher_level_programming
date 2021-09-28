#!/usr/bin/python3
"""
Module 102-square
Defines a square based on module 4-square
"""


class Square:
    """Represents blueprint for a square"""

    def __init__(self, size=0):
        """
        Initialize the sqaure.
        Args:
            size (int): length of the square's side.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the current square area
        """
        return self.__size**2

    @property
    def size(self):
        """
        Getter
        Retrieves the square's size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        Set the square's size.
        Args:
            value (int): length of the square's side.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __gt__(self, other):
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size
