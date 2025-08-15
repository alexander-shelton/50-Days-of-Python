#!/usr/bin/env python3
import unittest
from day_26 import sort_words, string_length

class TestDay26(unittest.TestCase):

    # Day 26: Sort Words  
    def test_sort_words(self):
        words = "love life"
        expected = ['e, f, i, l, o, v']
        pass
        
    ## Extra Challenge: Length of Words  
    def test_string_length(self):
        s = 'Hi my name is Richard'
        expected = {'Hi': 2, 'my': 2, 'name': 4, 'is': 2, 'Richard': 7}
        pass

if __name__ == '__main__':
    unittest.main()