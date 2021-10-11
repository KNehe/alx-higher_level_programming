#!/usr/bin/python3
"""
Module 10-square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from Rectangle
    methods:
        __init__(self, size)
    """
    def __init__(self, size):
        """initialize square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
