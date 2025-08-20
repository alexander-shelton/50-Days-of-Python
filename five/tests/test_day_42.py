#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_42 import spelling_checker, set_alarm

class TestDay42(unittest.TestCase):

    # Day 42: Spelling Checker  
    def test_spelling_checker(self):
        with patch('builtins.input', side_effect=['test']):
            result = spelling_checker()
            expected = 'Your word is, test'
            self.assertEqual(result, expected)
        with patch('builtins.input', side_effect=['teste', 'yes']):
            result = spelling_checker()
            expected = 'Your word is, test'
            self.assertEqual(result, expected)
            
    ## Extra Challenge: Set Alarm
    def test_set_alarm(self):
        pass

if __name__ == '__main__':
    unittest.main()