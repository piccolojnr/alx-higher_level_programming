#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    RM = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    prev = 0

    for s in reversed(roman_string):
        v = RM.get(s, 0)

        if v < prev:
            res -= v
        else:
            res += v

        prev = v

    return res
