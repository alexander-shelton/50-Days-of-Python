#!/usr/bin/env python3
import unittest
from day_48 import search_binary

class TestDay48(unittest.TestCase):

    # Day 48: Binary Search  
    def test_search_binary(self):
        num = 22
        nums = [12, 34, 56, 78, 98, 22, 45, 13]
        self.assertEqual(search_binary(num, nums), 2)

if __name__ == '__main__':
    unittest.main()