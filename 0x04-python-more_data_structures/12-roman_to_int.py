#!/usr/bin/python3

def roman_to_int(roman_string):
    """converts a Roman numeral to an integer"""
    rom_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if roman_string is None:
        return 0
    num = 0
    old = 0
    for char in roman_string:
        for key, value in rom_int.items():
            if char == key:
                if value <= old:
                    num += value
                    old = value
                    break
                else:
                    num += value - (2 * old)
                    old = value
                    break
    return num



roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MCMLX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
