#!/usr/bin/python3

"""
Module 6-rectangle
Defines a rectangle
Handles instance count
"""


class Rectangle:
    """
    Defines a rectangle
    Private attributes width and height
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initialize width and height """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Returns area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """ Returns perimeter of a rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return 2*(self.width + self.height)

    def __str__(self):
        """return string object of rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join("#" * self.width for row in range(self.height))

    def __repr__(self):
        """Returns canonical string representation
            of a rectangle with #"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ Prints a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
