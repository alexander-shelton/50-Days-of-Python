#!/usr/bin/env python3
import unittest
from day_35 import check_pangram, find_index

class TestDay35(unittest.TestCase):

    # Day 35: Pangram
    def test_check_pangram(self):
        string = "the quick brown fox jumps over a lazy dog"
        self.assertTrue(check_pangram(string))
        
    ## Extra Challenge: Find my Position
    def test_find_index(self):
        nums = [1, 2, 4, 6, 7, 7] 
        num = 7
        expected = [4, 5]
        self.assertEqual(find_index(nums, num), expected)
        nums = [1, 2, 4, 6, 7, 7]
        num = 8
        expected = [8, 8, 8, 8, 8, 8]
        self.assertEqual(find_index(nums, num), expected)

if __name__ == '__main__':
    unittest.main()