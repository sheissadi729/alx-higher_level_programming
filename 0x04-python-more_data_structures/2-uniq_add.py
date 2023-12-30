#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique integers in a list"""
    result = 0
    new_list = set(my_list)
    for i in new_list:
        result += i
    return result
