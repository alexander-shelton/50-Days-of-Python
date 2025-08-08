#!/usr/bin/env python3
import unittest
from day_1 import divide_or_square, longest_value

class TestDay1(unittest.TestCase):

    # Day 1: Division and Square-root
    def test_divide_or_square(self):
        self.assertEqual(divide_or_square(10), 3.1622776601683795)
        self.assertEqual(divide_or_square(8), 3)

    # Extra Challenge: Longest Value
    def test_longest_value(self):
        fruits = {'fruit': 'apple', 'color': 'green'}
        self.assertEqual(longest_value(fruits), 'apple')

if __name__ == '__main__':
    unittest.main()