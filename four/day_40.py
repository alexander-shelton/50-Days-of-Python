#!/usr/bin/env python3
#
# Day 40: Pig Latin

def translate(words: str) -> str:
    latin = []
    for word in words.split(' '):
        if word[0] in ('a', 'e', 'i', 'o', 'u'):
            latin.append(f"{word}yay")
        else:
            latin.append(f"{word[1:]}{word[0]}ay")
    return ' '.join(latin)