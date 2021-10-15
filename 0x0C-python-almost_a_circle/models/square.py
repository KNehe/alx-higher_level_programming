#!/usr/bin/python3
"""
Module square
With Square classs
That inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class definition
    Methods:
        def __init__(self,size,x,y,id)
        def __str__(self)
        def update(self, *args, **kwargs)
        def to_dictionary(self)
    Getter:
        def size(self)
    Setter:
        def size(self, value)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize square
        Invokes super class
        with width, height, x, y, and id
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Overridding __str__ for square
        to priduce '[Square] (<id>) <x>/<y> - <size>'
        """
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update square using non and keyword
        arguments
        """
        if args:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                else:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dict representation of square"""
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
