#!/usr/bin/env python3
#
# Day 20: Capitalize First Letter
from string import ascii_uppercase

def capitalize(string: str) -> str:
    return ' '.join([word.capitalize() for word in string.split(' ')])

## Extra Challenge: Reversed List
def reversed_list(str1: str) -> list:
    return [word[::-1] for word in str1.split(' ') if word != word.lower()]