#!/usr/bin/env python3
#
# Day 7: A String Range

def string_range(num: int) -> str:
    return  '.'.join(str(i) for i in range(num))


# Extra Challenge: Dictionary of Names
def names_starting_with_letter(names: list, letter: str) -> dict:
    names_dict = {}
    for name in names:
        if name.lower().startswith(letter):
            if names_dict.get(name):
                names_dict[name] += 1
            else:
                names_dict[name] = 1
    return names_dict