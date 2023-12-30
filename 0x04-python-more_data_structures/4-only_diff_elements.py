#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """returns a set of all elements present in only one set"""
    new_set = set_1 ^ set_2
    return new_set

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
