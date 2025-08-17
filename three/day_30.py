#!/usr/bin/env python3
# 
# Day 30: Most Repeated Name  
from collections import Counter

def repeated_name(names: list) -> tuple:
    return max(Counter(names).most_common(1))

    
## Extra Challenge: Sort by Last Name  
def sorted_names(names: list) -> list:
    return sorted([' '.join(name.split(' ')[::-1]) for name in names])