#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_0, a_1, b_0, b_1 = 0, 0, 0, 0
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    res_1, res_2 = 0, 0

    if len_a == 1:
        a_0 = tuple_a[0]
    if len_a >= 2:
        a_0 = tuple_a[0]
        a_1 = tuple_a[1]
    if len_b == 1:
        b_0 = tuple_b[0]
    if len_b >= 2:
        b_0 = tuple_b[0]
        b_1 = tuple_b[1]
    res_1 = a_0 + b_0
    res_2 = a_1 + b_1
    return res_1, res_2
