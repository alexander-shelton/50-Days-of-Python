#!/usr/bin/env python3
#
# Day 26: Sort Words  

def sort_words(words: str) -> list:
    return [', '.join(sorted(list(set(char for char in words.replace(' ', '')))))]


## Extra Challenge: Length of Words  
def string_length(words: str) -> dict:
    return dict((word,len(word)) for word in words.split(' '))