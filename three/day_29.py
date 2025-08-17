#!/usr/bin/env python3
#
# Day 29: Middle Figure  

def middle_figure(a: str, b: str) -> str:
    string = (a+b).replace(' ', '')
    return string[len(string)//2] if len(string) % 2 != 0 else "no middle figure"