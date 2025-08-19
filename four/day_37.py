#!/usr/bin/env python3
#
# Day 37: Count the Vowels
from collections import Counter

def count_the_vowels(string: str) -> int|str:
    if type(string) != str:
        return "invalid input"
    count = 0
    for char in set(string):
        if char in ('a', 'e', 'i', 'o', 'u'):
            count += 1
    return count if count > 0 else "The string has no vowels."