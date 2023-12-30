#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if not a_dictionary:
        return None
    high_value = 0
    high_key = None
    for key, value in a_dictionary.items():
        if value > high_value:
            high_value = value
            high_key = key
    return high_key
