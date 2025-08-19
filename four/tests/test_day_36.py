#!/usr/bin/env python3
import unittest
from day_36 import count, sum_nested_dict

class TestDay36(unittest.TestCase):

    # Day 36: Count String
    def test_count(self):
        string = "hello"
        expected = {'h':1, 'e':1, 'l':2, 'o':1}
        self.assertEqual(count(string), expected)

    ## Extra Challenge: Sum a Nested Dictionary
    def test_sum_nested_dict(self):
        nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}, 'g': 5}
        expected = 15
        self.assertEqual(sum_nested_dict(nested_dict), expected)

if __name__ == '__main__':
    unittest.main()