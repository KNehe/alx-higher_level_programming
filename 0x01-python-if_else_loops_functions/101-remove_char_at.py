#!/usr/bin/python3


# Using slicing
def remove_char_at(str, n):
    return (str[:n] + str[n+1:] if n >= 0 else str)


# Using iteration
def remove_char_at2(str, n):
    copy = ""
    for i in range(len(str)):
        if i != n:
            copy += str[i]
    return (copy)
