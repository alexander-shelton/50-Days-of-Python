#!/usr/bin/env python3
import unittest
from day_20 import capitalize, reversed_list

class TestDay20(unittest.TestCase):

    # Day 20: Capitalize
    def test_capitalize(self):
        string = "i like learning"
        expected = "I Like Learning"
        self.assertEqual(capitalize(string), expected)

    ## Extra Challenge: Reversed List
    def test_reversed_list(self):
        str1 = 'leArning is hard, bUt if You appLy youRself you can achieVe success'
        expected = ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']
        self.assertEqual(reversed_list(str1), expected)

if __name__ == "__main__":
    unittest.main()