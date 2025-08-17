#!/usr/bin/env python3
import unittest
from day_29 import middle_figure

class TestDay29(unittest.TestCase):

    # Day 29: Middle Figure  
    def test_middle_figure(self):
        a = "make love"
        b = "not wars"
        expected = "e"
        self.assertEqual(middle_figure(a, b), expected)
        
if __name__ == '__main__':
    unittest.main()