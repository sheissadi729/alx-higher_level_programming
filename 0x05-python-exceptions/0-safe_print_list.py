#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints x elements of a list"""
    try:
        i = 0
        for element in range(x):
            print(my_list[element], end="")
            i += 1
    except IndexError:
        return i
    finally:
        print()
    return x
