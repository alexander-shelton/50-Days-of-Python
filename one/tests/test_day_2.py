#!/usr/bin/env python3
import unittest
from day_2 import convert_add, check_duplicates

class TestDay2(unittest.TestCase):

    # Day 2: Strings to Integers 
    def test_convert_add(self):
        example_list = ["1", "3", "5"]
        self.assertEqual(convert_add(example_list), 9)

    # Extra Challenge: Duplicate Names
    def test_check_duplicates(self):
        fruits = ['apple', 'orange', 'banana', 'apple', 'banana']
        names = ['Yoda', 'Moses', 'Joshua', 'Mark']
        self.assertEqual(check_duplicates(fruits), ["apple", "banana"])
        self.assertEqual(check_duplicates(names), "no duplicates")

if __name__ == '__main__':
    unittest.main()