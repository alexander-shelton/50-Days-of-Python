#!/usr/bin/env python3
import unittest
from day_9 import biggest_odd, zeros_last

class TestDay9(unittest.TestCase):
    # Day 9: Biggest Odd Number
    def test_biggest_odd(self):
        num = "23569"
        expected = 9
        self.assertEqual(biggest_odd(num), expected)

    # Extra Challenge: Zeros to the End
    def test_zero_last(self):
        nums = [1, 4, 6, 0, 7, 0, 9]
        expected = [1, 4, 6, 7, 9, 0, 0]
        self.assertEqual(zeros_last(nums), expected)
        nums = [2, 1, 4, 7, 6]
        expected = [1, 2, 4, 6, 7]
    
if __name__ == '__main__':
    unittest.main()