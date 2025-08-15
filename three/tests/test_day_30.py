#!/usr/bin/env python3
import unittest
from day_30 import repeated_name, sorted_names

class TestDay30(unittest.TestCase):

    # Day 30: Most Repeated Name
    def test_repeated_name(self):
        name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
        expected = ("Peter", 3)
        pass
        
    ## Extra Challenge: Sort by Last Name
    def test_sorted_names(self):
        names = ["Beyoncé  Knowles ", "Alicia Keys ", "Katie Perry ", "Chris Brown ", "Tom Cruise "]
        expected = ['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Knowles Beyonce', 'Perry Katie']
        pass

if __name__ == '__main__':
    unittest.main()