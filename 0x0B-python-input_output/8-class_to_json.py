#!/usr/bin/python3
"""
Module 8-class_to_json
Contains a function that returns the dictionary
description with simple data structure (list,
dictionary, string, integer and boolean) for
JSON serialization of an object:
"""


def class_to_json(obj):
    return obj.__dict__
