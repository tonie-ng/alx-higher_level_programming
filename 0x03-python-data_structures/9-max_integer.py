#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    result = 0
    for val in my_list:
        if val > result:
            result = val
    return result
