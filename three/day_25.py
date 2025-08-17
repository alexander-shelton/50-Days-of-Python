#!/usr/bin/env python3
#
# Day 25: All the Same

from typing import Union

def all_the_same(args: Union[str,list,tuple]) -> bool:
    if isinstance(args, (str, list, tuple)):
        return (i == args[0] for i in args)
    else:
        raise TypeError("Input must be a string, a list, or a tuple.")

        
## Extra Challenge:  Reverse a String
def read_backwards(string: str) -> str:
    return ' '.join(string.split(' ')[::-1])