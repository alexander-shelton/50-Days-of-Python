#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_24 import average_calories, nested_lists

class TestDay24(unittest.TestCase):

    # Day 24: Average Calories  
    def test_average_calories(self):
        with patch('builtins.input', side_effect=['2500', '1850', '2110', 'done']):
            result = average_calories()
            expected = (2500 + 1850 + 2110) / 3
            self.assertEqual(result, expected)
        
    ## Extra Challenge:  Create a Nested List
    def test_nested_lists(self):
        expected = [[1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]]
        self.assertEqual(nested_lists([1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]), expected)
        expected = "Invalid arguments. Please check your arguments."
        self.assertEqual(nested_lists((1, 2, 3, 5), [1, 2, 3, 4], [1, 3, 4, 5]), expected)

if __name__ == '__main__':
    unittest.main()