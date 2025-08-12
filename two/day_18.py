#!/usr/bin/env python3
#
# Day 18: Any Number of Arguments

def called_any_number(*args) -> float:
    return sum([*args]) / len([*args])


## Extra Challenge: Add and Reverse


def add_reverse(nums1: list, nums2: list) -> list:
    new_list = []
    if len(nums1) != len(nums2):
        return "The lists are not of equal length."
    for i in range(0, len(nums1)):
        new_list.append(nums1[i] + nums2[i])
        new_list.reverse()
    return new_list