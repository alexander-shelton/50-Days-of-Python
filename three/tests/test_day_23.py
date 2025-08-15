#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_23 import calculator, multiply_words

class TestDay23(unittest.TestCase):

    # Day 23: Simple Calculator
    def test_add(self):
        with patch("builtins.input", side_effect=['a', 'y', 100, 100]):
            result = calculator()
            expected = "100 + 100 = 200"
            self.assertEqual(result, expected)

    def test_subtract(self):
        with patch("builtins.input", side_effect=['s', 'y', 100, 100]):
            result = calculator()
            expected = "100 - 100 = 0"
            self.assertEqual(result, expected)
        
    def test_divide(self):
        with patch("builtins.input", side_effect=['d', 'y', 100, 100]):
            result = calculator()
            expected = "100 / 100 = 1"
            self.assertEqual(result, expected)
    
    def test_zerodivision_error(self):
        with patch("builtins.input", side_effect=['d', 'y', 100, 0]):
            result = calculator()
            expected = "Sorry you can not divide a number by 0"
            self.assertEqual(result, expected)

    def test_multiply(self):
        with patch("builtins.input", side_effect=['m', 'y', 100, 100]):
            result = calculator()
            expected = "100 * 100 = 10000"
            self.assertEqual(result, expected)

    def test_multiply_words(self):
        string = "love live and laugh"
        expected = "240: love (4), live (4), and (3), laugh (5)"
        self.assertEqual(multiply_words(string), expected)
        string = "Hate war love Peace"
        expected = "12: war (3), love (4)"
        self.assertEqual(multiply_words(string), expected)

if __name__ == '__main__':
    unittest.main()