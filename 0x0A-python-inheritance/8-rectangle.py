#!/usr/bin/python3

"""
Module 8-rectangle
inherits from BaseGeometry,
(7-base_geometry.py).
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle whose super class is BaseGeometry"""

    def __init__(self, width, height):
        """initialize width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
