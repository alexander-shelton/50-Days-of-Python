#!/usr/bin/env python3
import unittest
from day_37 import count_the_vowels

class TestDay37(unittest.TestCase):

    # Day 37: Count the Vowels
    def test_count_the_vowels1(self):
        string = 50
        expected = "invalid input"
        self.assertEqual(count_the_vowels(string), expected)
    
    def test_count_the_vowels2(self):
        string = "hello"
        expected = 2
        self.assertEqual(count_the_vowels(string), expected)
    
    def test_count_the_vowels3(self):
        string = "saas"
        expected = 1
        self.assertEqual(count_the_vowels(string), expected)
    
    def test_count_the_vowels4(self):
        string = "sly"
        expected = "The string has no vowels."
        self.assertEqual(count_the_vowels(string), expected)

if __name__ == '__main__':
    unittest.main()