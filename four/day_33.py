#!/usr/bin/env python3
# 
# Day 33: List Intersection

def inter_section(list1: list, list2: list) -> tuple:
    inter_list = [num for num in list1 if num in list2]
    inter_list[0], inter_list[-1] = inter_list[-1], inter_list[0]
    return tuple(inter_list)


## Extra Challenge: Set or List
import timeit

# Set search
set_test = '''
a = range(10000000)
x = set(a)
i = 999999
i in x
'''

set_search_time = timeit.timeit(stmt=set_test, number=1000)

# List search
list_test = '''
a = range(10000000)
y = list(a)
i = 999999
i in y
'''

list_search_time = timeit.timeit(stmt=list_test, number=1000)

print(f"Set search time: {set_search_time}")
print(f"List search time: {list_search_time}")