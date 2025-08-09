#!/usr/bin/env python3
#
# Day 11: Are They Equal?
from collections import Counter

def equal_strings(str1: str, str2: str) -> bool:
    return Counter(str1) == Counter(str2)
    

def swap_values(nums: list) -> list:
    nums.insert(0, nums.pop())
    nums.append(nums.pop(1))
    return nums