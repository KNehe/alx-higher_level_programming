#!/usr/bin/python3

"""
Module 1-my_list.py
that prints the list,
but sorted (ascending sort)
"""


class MyList(list):

    """ Custom list that inherits from list """
    def print_sorted(self):
        """ prints list in ascending order"""
        print(sorted(self))
