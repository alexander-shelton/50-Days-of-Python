#!/usr/bin/env python3
import unittest
from day_3 import register_check, sort_list

class TestDay3(unittest.TestCase):

    # Day 3: Register Check 
    def test_register_check(self):
        register = {'Michael': 'yes', 'John': 'no', 'Peter': 'yes', 'Mary': 'yes'}
        self.assertEqual(register_check(register), 3)

    
    def test_sort_list(self):
        names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
        expected = ('kerry', 'dickson', 'carol', 'adam')
        self.assertEqual(sort_list(names), expected)

if __name__ == '__main__':
    unittest.main()