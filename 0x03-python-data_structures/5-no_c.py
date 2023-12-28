#!/usr/bin/python3

def no_c(my_string):
    """removes all characters c and C from a string"""
    new_string = "".join([c for c in my_string if c not in "cC"])
    return new_string
