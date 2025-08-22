#!/usr/bin/env python3
import unittest
from day_45 import analyse_string

class TestDay45(unittest.TestCase):

    # Day 45: Words & Special Characters
    def test_analyse_string(self):
        string = '"Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2"'
        result = analyse_string(string)
        numeric = result['numeric']
        special = result['special']
        total = result['total']
        self.assertEqual(numeric, 1)
        self.assertEqual(special, 7)
        self.assertEqual(total, 141)

if __name__ == '__main__':
    unittest.main()