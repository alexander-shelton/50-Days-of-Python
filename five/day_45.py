#!/usr/bin/env python3
#
# Day 45: Words & Special Characters

from string import punctuation, digits

punctuation = [punc for punc in punctuation]
digits = [n for n in digits]

def analyse_string(string: str) -> dict:
    unique_chars = {'special': 0, 'numeric': 0, 'total': 0}
    for word in string.split(' '):
        for char in word:
            unique_chars['total'] += 1
            if char in punctuation:
                unique_chars['special'] += 1
                punctuation.remove(char)
            elif char in digits:
                unique_chars['numeric'] += 1
                digits.remove(char)
    return unique_chars