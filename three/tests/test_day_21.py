#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_21 import make_tuples, even_or_average

class TestDay21(unittest.TestCase):

    # Day 21: List of Tuples
    def test_make_tuples(self):
        a = [1, 2, 3, 4]
        b = [5, 6, 7, 8]
        expected = [(1, 5), (2, 6), (3, 7), (4, 8)]
        self.assertEqual(make_tuples(a, b), expected)
        c = [1, 2, 3, 4]
        d = [5, 6, 7]
        self.assertEqual(make_tuples(c, d), ValueError)
        
    ## Extra Challenge: Even Number or Average
    def test_even_or_average(self):
        with patch("builtins.input", side_effect=[5, 4, 20, 9, 15]):
            result = even_or_average()
            expected = 20
            self.assertEqual(result, expected)
        with patch("builtins.input", side_effect=[5, 3, 21, 9, 17]):
            result = even_or_average()
            expected = 11.0
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()