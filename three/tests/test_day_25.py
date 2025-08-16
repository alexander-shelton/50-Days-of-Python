#!/usr/bin/env python3
import unittest
from day_25 import all_the_same, read_backwards

class TestDay25(unittest.TestCase):

    # Day 25: All the Same  
    def test_all_the_same(self):
        arg = ["Mary", "Mary", "Mary"]
        self.assertTrue(all_the_same(arg))
        arg = 'bbbbbbbbbb'
        self.assertTrue(all_the_same(arg))
        arg = ('a', 'a', 'a', 'a')
        self.assertTrue(all_the_same(arg))
        
    ## Extra Challenge:  Reverse a String
    def test_read_backwards(self):
        str1 = "the love is real"
        expected = "real is love the"
        self.assertEqual(read_backwards(str1), expected)

if __name__ == '__main__':
    unittest.main()