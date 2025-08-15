#!/usr/bin/env python3
import unittest
from day_27 import unique_numbers, difference

class TestDay27(unittest.TestCase):

    # Day 27: Unique Numbers  
    def test_unique_numbers(self):
        nums = [1, 2, 4, 5, 6, 7, 8, 8]
        expected = [1, 2, 4, 5, 6, 7, 8, 8]
        pass
        
    ## Extra Challenge: Difference of Two Lists
    def test_difference(self):
        a = [1, 2, 4, 5, 6]
        b = [1, 2, 5, 7, 9]
        expected = [4, 6, 7, 9]
        pass

if __name__ == '__main__':
    unittest.main()