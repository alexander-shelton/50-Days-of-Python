#!/usr/bin/env python3
#
# Day 4: Only Floats

def only_floats(a, b) -> int:
    total_floats = 0
    total_floats += 1 if type(a) == float else 0
    total_floats += 1 if type(b) == float else 0
    return total_floats


# Extra Challenge: Index of the Longest Word 
def word_index(str_list:list) -> int:
    max_length = len(max(str_list, key=len))
    indices = [i for i, word in enumerate(str_list) if len(word) == max_length]

    return indices[0] if len(indices) == 1 else 0