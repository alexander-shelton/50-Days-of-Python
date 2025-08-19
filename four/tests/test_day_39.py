#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_39 import generate_password

class TestDay39(unittest.TestCase):

    # Day 39: Password Generator
    @patch('builtins.input', side_effect=['1'])
    def test_generate_password_weak(self, mock_input):
        self.assertEqual(len(generate_password()), 5)

    @patch('builtins.input', side_effect=['2'])
    def test_generate_password_strong(self, mock_input):
        self.assertEqual(len(generate_password()), 8)

    @patch('builtins.input', side_effect=['3'])
    def test_generate_password_very_strong(self, mock_input):
        self.assertEqual(len(generate_password()), 12)

    @patch('builtins.input', side_effect=['a'])
    def test_generate_password_very_strong(self, mock_input):
        self.assertEqual(generate_password(), "Invalid option. Please try again and select a valid option. e.g. 1, 2, 3")

if __name__ == '__main__':
    unittest.main()