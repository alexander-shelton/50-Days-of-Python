#!/usr/bin/env python3
import unittest
from day_38 import guess_a_number, missing_numbers

class TestDay38(unittest.TestCase):

    # Day 38: Guess a Number  
    def test_guess_a_number(self):
        pass

    ## Extra Challenge: Find Missing Numbers
    def test_missing_numbers(self):
        list1 = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,  
            18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]  
        expected = [4, 8, 10, 13, 16, 29, 30]
        self.assertEqual(missing_numbers(list1), expected)

if __name__ == '__main__':
    unittest.main()