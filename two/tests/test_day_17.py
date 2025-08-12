#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_17 import user_name, sort_length

class TestDay17(unittest.TestCase):

    # Day 17: User Name
    def test_user_name(self):
        with patch('builtins.input', side_effect=['alexander']):
            result = user_name()
            expected_name = "rednaxela"
            nums = [i for i in range(10)]
            name = result[:-1]
            random_num = int(result[-1])
            self.assertEqual(name, expected_name)
            self.assertIn(random_num, nums)
        
    # Day 17: Sort Length
    def test_sort_length(self):
        names  = [ "Peter",  "Jon", "Andrew"] 
        expected = ['Jon', 'Peter', 'Andrew']
        self.assertEqual(sort_length(names), expected)

if __name__ == "__main__":
    unittest.main()