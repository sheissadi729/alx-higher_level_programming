#!/usr/bin/python3

def safe_print_integer_err(value):
    '''prints an integer'''
    try:
        print("{:d}".format(value))
    except ValueError as ve:
        print("Exception:", ve)
        return False
    except TypeError as te:
        print("Exception:", te)
        return False
    return True
