#!/usr/bin/env python3
import unittest
from day_16 import sum_list, reversed_list

class TestDay16(unittest.TestCase):

    # Day 16: Sum List
    def test_sum_list(self):
        nested_list = [[2, 4, 5, 6], [2, 3, 5, 6]]
        expected = 33
        self.assertEqual(sum_list(nested_list), expected)
        

    # Day 16: Reversed List
    def test_reversed_list(self):
        nested_list = [[12, 34, 56, 67], [34, 68, 78]]
        expected = [34, 67, 78]
        self.assertEqual(reversed_list(nested_list), expected)

if __name__ == "__main__":
    unittest.main()