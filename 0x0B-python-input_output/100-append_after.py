#!/usr/bin/python3
"""Module 100-append_after.py"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        res = f.readlines()

    with open(filename, mode='w', encoding='utf-8') as f:
        new = []
        for i in range(len(res)):
            new.append(res[i])
            if search_string in res[i]:
                new.append(new_string)
        f.writelines(new)
