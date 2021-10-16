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
        to_json_string(list_dictionaries)
        save_to_file(cls, list_objs)
        from_json_string(json_string)
        load_from_file(cls)
        create(cls, **dictionary)
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
        """Convert list_dictionaries to json"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string
        representation of list_objs to a file
        """
        objs = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for ob in list_objs:
                objs.append(cls.to_dictionary(ob))
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """Converts json string to object"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Converts a dictionary to an instance"""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        if cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from file"""
        filename = cls.__name__ + ".json"
        objs = []
        try:
            with open(filename, "r") as f:
                obj_ls = cls.from_json_string(f.read())
                for i, j in enumerate(obj_ls):
                    objs.append(cls.create(**obj_ls[i]))
        except Exception:
            pass
        return objs
