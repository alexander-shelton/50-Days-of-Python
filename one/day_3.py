#!/usr/bin/env python3
#
# Day 3: Register Check 

def register_check(student_dict: dict) -> int:
    return len([value for value in student_dict.values() if value == 'yes'])


# Extra Challenge: Lowercase Names 
def sort_list(str_list:list) -> tuple:
    return tuple(sorted([name for name in str_list if name == name.lower()], reverse=True))