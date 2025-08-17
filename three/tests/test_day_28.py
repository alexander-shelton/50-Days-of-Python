#!/usr/bin/env python3
import unittest
from day_28 import index_position, largest_number

class TestDay28(unittest.TestCase):

    # Day 28: Return Indexes
    def test_index_position(self):
        string = "LovE"
        expected = [1, 2]
        self.assertEqual(index_position(string), expected)
        
    ## Extra Challenge: Largest Number
    def test_largest_number(self):
        nums = [3, 67, 87, 9, 2]
        expected = "The largest number is: 9,877,632"
        self.assertEqual(largest_number(nums), expected)

if __name__ == '__main__':
    unittest.main()