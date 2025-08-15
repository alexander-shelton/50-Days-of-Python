#!/usr/bin/env python3
import unittest
from day_24 import average_calories, nested_lists

class TestDay24(unittest.TestCase):

    # Day 24: Average Calories  
    def test_average_calories(self):
        pass
        
    ## Extra Challenge:  Create a Nested List
    def test_nested_lists(self):
        args = [1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]
        expected = [[1, 2, 3, 5], [1, 2, 3, 4], [1, 3, 4, 5]]
        #self.assertEqual(nested_lists(args), expected)
        args = (1, 2, 3, 5), [1, 2, 3, 4], [1, 3, 4, 5]
        expected = "Invalid arguments. Please check your arguments."

if __name__ == '__main__':
    unittest.main()