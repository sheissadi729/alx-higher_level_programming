#!/usr/bin/python3

def multiple_returns(sentence):
    """ returns a tuple with the length of a string and its first character"""
    if sentence == "":
        my_tuple = len(sentence), None
    else:
        my_tuple = len(sentence), sentence[0]
    return my_tuple
