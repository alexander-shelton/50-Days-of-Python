#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_10 import hide_password, convert_numbers

class TestDay10(unittest.TestCase):
    # Day 10: Hide Password
    def test_hide_password(self):
        with patch('builtins.input', side_effect=['Passw0rd123']):
            result = hide_password()
            expected = '*' * len('Passw0rd123')
            self.assertEqual(result, expected)

    # Extra Challenge: Convert Numbers
    def test_convert_numbers(self):
        nums = [1000000, 2356989,  2354672,  9878098]
        expected = ['1,000,000', '2,356,989', '2,354,672', '9,878,098']
        self.assertEqual(convert_numbers(nums), expected)
    
if __name__ == '__main__':
    unittest.main()