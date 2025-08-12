#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_15 import same_in_reverse, your_age

class TestDay15(unittest.TestCase):

    # Day 15: Same in Reverse
    def test_same_in_reverse(self):
        self.assertTrue(same_in_reverse("level"))
        self.assertFalse(same_in_reverse("hello"))

    # Day 15: Your Age
    def test_your_age(self):
        with patch('builtins.input', side_effect=['tim']):
            result = your_age()
            self.assertEqual(result, "Hi, Tim, you are 34 years old.")
        with patch('builtins.input', side_effect=['alex', 31]):
            result = your_age()
            self.assertEqual(result, "Hi, Alex, you are 31 years old.")

if __name__ == "__main__":
    unittest.main()