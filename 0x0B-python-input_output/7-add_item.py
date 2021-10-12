#!/usr/bin/python3
"""
Module 7-add_item
A script that adds all arguments to a
Python list, and then save them to a file
"""


from sys import argv
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    content = load(filename)
except Exception:
    content = []
save(content + argv[1:], filename)
