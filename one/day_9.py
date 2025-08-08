#!/usr/bin/env python3
#
# Day 9: Biggest Odd Number

def biggest_odd(nums: str) -> int:
    return max([int(num) for num in nums if int(num) % 2 != 0])


# Extra Challenge: Zeros to the End
def zeros_last(nums: list) -> list:
    if 0 in nums:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
        return nums
    else:
        return sorted(nums)