#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_31 import longest_word, create_user

class TestDay31(unittest.TestCase):

    # Day 31: Longest Word
    def test_longest_word(self):
        words = ['Java', 'JavaScript', 'Python']
        expected = [10, 'JavaScript']
        self.assertEqual(longest_word(words), expected)
        
    ## Extra Challenge: Create User
    def test_create_user(self):
        with patch("builtins.input", side_effect=['Peter', 18, 'love', 'Peter', 18, 'love']):
            result = create_user()
            expected = 'Logged in successfully'
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()