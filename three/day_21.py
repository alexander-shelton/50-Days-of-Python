#!/usr/bin/env python3
# 
# Day 21: List of Tuples

def make_tuples(a: list, b: list):
    if len(a) != len(b):
        return ValueError
    return list(zip(a, b))


## Extra Challenge: Even Number or Average
def even_or_average():
    total, count = 0, 0
    max_even = None
    while count < 5:
        try:
            num = int(input("Enter a number: "))
            if num % 2 == 0:
                if max_even is None or num > max_even:
                    max_even = num
            total += num
            count += 1
        except ValueError:
            print("Please enter a valid number.")
    return total / count if max_even is None else max_even