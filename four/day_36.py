#!/usr/bin/env python3
#
# Day 36: Count Sring

from collections import Counter

def count(string: str) -> dict:
    return Counter(string)
    
## Extra Challenge: Sum a Nested Dictionary
def sum_nested_dict(nested_dict: dict) -> int:
    summed = 0
    for val in nested_dict.values():
        if isinstance(val, dict):
            summed += sum_nested_dict(val)
        else:
            summed += val
    return summed