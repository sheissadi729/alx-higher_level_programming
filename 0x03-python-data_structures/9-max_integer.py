#!/usr/bin/python3

def max_integer(my_list=[]):
    """ finds the biggest integer of a list"""
    maxi = 0
    for num in my_list:
        if num > maxi:
            maxi = num
    return maxi
