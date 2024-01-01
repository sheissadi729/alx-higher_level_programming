#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    ''' executes a function safely'''
    try:
        return fct(*args)
    except ZeroDivisionError as zde:
        print("Exception:", zde, file=sys.stderr)
        return None
    except IndexError as ie:
        print("Exception:", ie, file=sys.stderr)
        return None
