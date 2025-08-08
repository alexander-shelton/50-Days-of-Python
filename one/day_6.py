#!/usr/bin/env python3
#
# Day 6: User Name Generator

def user_name(email: str) -> str:
    return email.split('@')[0]


# Extra Challenge: Zero Both Ends
def zeroed(nums: list) -> list:
    for i in (0, -1):
        nums[i] = 0
    return nums