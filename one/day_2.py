#!/usr/bin/env python3
#
# Day 2: Strings to Integers 

def convert_add(str_list: list) -> list:
    return sum([int(char) for char in str_list])


# Extra Challenge: Duplicate Names 
def check_duplicates(str_list: list) -> list:
    set_list = set(str_list)
    duplicates = []
    for _ in set_list:
        if str_list.count(_) > 1:
            duplicates.append(_)
    return sorted(duplicates) if len(duplicates) > 0 else "no duplicates"