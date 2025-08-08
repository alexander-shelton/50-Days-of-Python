#!/usr/bin/env python3
import unittest
from day_6 import user_name, zeroed

class TestDay6(unittest.TestCase):

    # Day 6: User Name Generator
    def test_user_name(self):
        example_email = "ben@gmail.com"
        self.assertEqual(user_name(example_email), 'ben')

    # Extra Challenge: Zero Both Ends
    def test_zeroed(self):
        example_list = [2, 5, 7, 8, 9]
        expected = [0, 5, 7, 8, 0]
        self.assertEqual(zeroed(example_list), expected)

if __name__ == '__main__':
    unittest.main()