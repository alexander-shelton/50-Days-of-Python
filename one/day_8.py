#!/usr/bin/env python3
#
# Day 8: Odd and Even
from typing import Union

def odd_even(nums: list) -> Union[int, float]:
    max_even = None
    min_odd = None
    for num in nums:
        if num % 2 == 0:
            if max_even is None or num > max_even:
                max_even = num
        else:
            if min_odd is None or num < min_odd:
                min_odd = num
    return max_even - min_odd


# Extra Challenge: List of Prime Numbers
def isprime(num):
    for n in range(2, int(num ** 0.5) + 1): 
        if num % n == 0:
            return False
    return True

def prime_numbers(num: int) -> list:
    primes = []
    for i in range(2, num):
        if isprime(i):
            primes.append(i)
    return primes