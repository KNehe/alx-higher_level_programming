#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        total = 0
        div = 0
        for t in my_list:
            x, t = t
            total += x * t
            div += t
        return total/div if div > 0 else 0
    return 0
