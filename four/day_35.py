#!/usr/bin/env python3
#
# Day 35: Pangram

from string import ascii_letters
from string import ascii_lowercase

def check_pangram(string: str) -> bool:
    for char in ascii_lowercase:
        if char not in string.lower():
            return False
    return True


## Extra Challenge: Find my Position
def find_index(nums: list, num: int) -> list:
    if nums.count(num) < 1:
        return [num] * len(nums)
    return [i for i, n in enumerate(nums) if n == num]