#!/usr/bin/env python3
#
# Day 17: User Name Generator
from random import randint

def user_name() -> str:
    return f"{input("Enter your name: ")[::-1]}{randint(0,9)}"

## Extra Challenge: Sort by Length
def sort_length(strings: list) -> list:
    return sorted(strings, key=len)