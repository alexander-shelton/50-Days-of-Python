#!/usr/bin/env python3
#
# Day 28: Return Indexes

def index_position(string: str) -> list:
    return [i for i in range(len(string)) if string[i].islower()]


## Extra Challenge: Largest Number
def largest_number(nums: list) -> str:
    return f"The largest number is: {int(''.join(map(str, sorted([int(n) for n in str(nums).strip('[,]').replace(',', '').replace(' ', '')], reverse=True)))):,}"