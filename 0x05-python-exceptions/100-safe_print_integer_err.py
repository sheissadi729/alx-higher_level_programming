#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    '''prints an integer'''
    try:
        print("{:d}".format(value))
    except ValueError as ve:
        print("Exception:", ve, file=sys.stderr)
        return False
    except TypeError as te:
        print("Exception:", te, file=sys.stderr)
        return False
    return True
