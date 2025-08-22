#!/usr/bin/env python3
#
# Day 48: Binary Search  

def search_binary(num: int, nums: list) -> int:
    nums = sorted(nums)
    first = 0
    last = len(nums) - 1
    while last >= first:
        mid = (first + last) // 2
        if nums[mid] == num:
            return mid
        elif nums[mid] < num:
            first = mid + 1
        else:
            last = mid - 1
    return False