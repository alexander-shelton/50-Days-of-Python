#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_34 import just_digits

class TestDay34(unittest.TestCase):

    # Day 21: List of Tuples
    def test_just_digits(self):
        expected = "1991, 2, 2000, 3, 2008"
        self.assertEqual(just_digits('./python.csv'), expected)

if __name__ == '__main__':
    unittest.main()