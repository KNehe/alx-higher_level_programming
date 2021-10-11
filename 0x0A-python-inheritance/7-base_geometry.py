#!/usr/bin/python3
"""
Module 7-base_geometry

Based on 5-base_geometry
"""


class BaseGeometry:
    """
    methods:
        area(self)
        integer_validation(self, name, value)
    """

    def area(self):
        """raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
