#!/usr/bin/env python3
import unittest
from day_18 import called_any_number, add_reverse

class TestDay18(unittest.TestCase):

    # Day 18: Called Any Number
    def test_called_any_number(self):
        expected = 37.0
        self.assertEqual(called_any_number(12, 90, 12, 34), expected)
        expected = 51.0
        self.assertEqual(called_any_number(12, 90), expected)

    ## Extra Challenge: Add Reverse
    def test_add_reverse(self):
        nums1 = [10, 12, 34]
        nums2 = [12, 56, 78]
        expected = [112, 22, 68]
        self.assertEqual(add_reverse(nums1, nums2), expected)
        nums1 = [10, 12, 34]
        nums2 = [12, 56]
        expected = "The lists are not of equal length."
        self.assertEqual(add_reverse(nums1, nums2), expected)
        


if __name__ == "__main__":
    unittest.main()