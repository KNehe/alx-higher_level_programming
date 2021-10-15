#!/usr/bin/python3
"""
Module base
The “base” of all other classes in this project
The goal of it is to manage id attribute
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert list_dictionaries to json"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
