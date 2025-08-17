#!/usr/bin/env python3
#
# Day 27: Unique Numbers

def unique_numbers(nums: list) -> list:
    nums_sum = sum(nums) + sum(set(nums))
    if nums_sum % 2 == 0:
        return nums
    return list(set(nums))

        
## Extra Challenge: Difference of Two Lists
def difference(a: list, b: list) -> list:
    return [char for char in (a+b) if char not in a and char in b or char in a and char not in b]