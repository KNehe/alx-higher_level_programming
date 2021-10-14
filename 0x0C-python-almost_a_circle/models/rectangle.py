#!/usr/bin/python3
"""
Module rectangle
Defines a rectangle
Inherits from base
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines a rectangle class
    That inherits from Base
    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
    Getters:
        width(self)
        height(self)
        x(self)
        y(self)
    Setter:
        width(self, value)
        height(self, value)
        x(slef, value)
        y(self, value)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle on creation"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter fro x field"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x field"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter fro y field"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for x field"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints self to stdout with '#'"""
        print("\n".join(["#" * self.__width for i in range(self.__height)]))
