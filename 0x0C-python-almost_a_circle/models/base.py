#!/usr/bin/python3
"""
Module base
The “base” of all other classes in this project
The goal of it is to manage id attribute
"""


class Base:
    """
    Base class
    methods:
        __init__(self,id)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing Base Class with id variable"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
