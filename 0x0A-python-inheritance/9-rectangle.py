#!/usr/bin/python3

"""
Module 9-rectangle
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

    def area(self):
        """Implements the area"""
        return self.__width * self.__height

    def __str__(self):
        """returns string representation"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
