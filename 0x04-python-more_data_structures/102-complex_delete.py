#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """deletes keys with a specific value in a dictionary"""
    for key, val in list(a_dictionary.items()):
        if val == value:
            del a_dictionary[key]
    return a_dictionary
