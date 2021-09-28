#!/usr/bin/python3
"""
Module 6-square
Defines a square based on module 5-square
"""


class Square:
    """Represents blueprint for a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the sqaure.
        Args:
            size (int): length of the square's side.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size
        self.position = position

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

    def my_print(self):
        s = self.__size
        p = self.__position[0]
        if s == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(s):
                for x in range(p):
                    print(" ", end="")
                for j in range(s):
                    print("#", end="")
                print()

    @property
    def position(self):
        """
        Getter
        Retrieves position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets position
        Args:
            value (int): coordinates
        """
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
