#!/usr/bin/env python3
#
# Day 22: Add Under_Score

def add_hash(text: str) -> str:
    return '#'.join(text.split(' '))

def add_underscore(text: str) -> str:
    return '_'.join(text.split('#'))

def remove_underscore(text: str) -> str:
    return ' '.join(text.split('_'))