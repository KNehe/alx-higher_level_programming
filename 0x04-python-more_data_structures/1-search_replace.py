#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        return [replace if i == search else i for i in my_list]
    return None
