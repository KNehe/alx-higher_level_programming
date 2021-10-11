#!/usr/bin/python3
"""
Module 11-square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle
    methods:
        __init__(self, size)
        __str__(self)
    """
    def __init__(self, size):
        """initializes square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """string representation"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
