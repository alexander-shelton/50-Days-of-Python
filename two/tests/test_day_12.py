#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_12 import count_dots, age_in_minutes

class TestDay12(unittest.TestCase):

    # Day 12: Count the Dots
    def test_count_dots(self):
        string = "h.e.l.p."
        expected = 4
        self.assertEqual(count_dots(string), expected)
        string = "he.lp."
        expected = 2
        self.assertEqual(count_dots(string), expected)

    ## Extra Challenge: Your Age in Minutes
    def test_age_in_minutes(self):
        with patch('builtins.input', side_effect=[1930]):
            age = age_in_minutes()
            expected = "You are 49,932,000 minutes old."
            self.assertEqual(age, expected)

if __name__ == "__main__":
    unittest.main()