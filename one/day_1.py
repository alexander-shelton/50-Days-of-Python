#!/usr/bin/env python3
#
# Day 1: Division and Square-root

from math import sqrt

def divide_or_square(num:int) -> int|float:
    return sqrt(num) if num % 5 == 0 else num % 5


# Extra Challenge: Longest Value
def longest_value(d: dict) -> str:
    longest = None
    for val in d.values():
        if longest is None or len(val) > len(longest):
            longest = val
    return longest