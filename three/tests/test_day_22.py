#!/usr/bin/env python3
import unittest
from day_22 import add_hash, add_underscore, remove_underscore

class TestDay22(unittest.TestCase):

    # Day 22: Add Under_Score
    def test_add_hash(self):
        text = "Python is awesome"
        expected = "Python#is#awesome"
        self.assertEqual(add_hash(text), expected)

    def test_add_underscore(self):
        text = "Python#is#awesome"
        expected = "Python_is_awesome"
        self.assertEqual(add_underscore(text), expected)

    def test_remove_underscore(self):
        text = "Python_is_awesome"
        expected = "Python is awesome"
        self.assertEqual(remove_underscore(text), expected)

if __name__ == '__main__':
    unittest.main()