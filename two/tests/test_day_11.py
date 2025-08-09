#!/usr/bin/env python3
import unittest
from day_11 import equal_strings, swap_values

class TestDay11(unittest.TestCase):

    # Day 11: Are They Equal?
    def test_equal_strings(self):
        str1 = "love"
        str2 = "evol"
        self.assertTrue(equal_strings(str1, str2))
        str3 = "false"
        str4 = "true"
        self.assertFalse(equal_strings(str3, str4))

    ## Extra Challenge: Swap Values
    def test_swap_values(self):
        nums = [2, 4, 67, 7]
        expected = [7, 4, 67, 2]
        self.assertEqual(swap_values(nums), expected)

if __name__ == '__main__':
    unittest.main()