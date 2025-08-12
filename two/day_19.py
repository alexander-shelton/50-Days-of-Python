#!/usr/bin/env python3
#
# Day 19: Words and Elements

def count_words(words: str) -> str:
    return len(words.split(' '))


def count_elements(words: str) -> int:
    return len(''.join(words.split(' ')))