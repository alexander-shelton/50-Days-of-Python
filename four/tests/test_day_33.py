#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_33 import inter_section, set_or_list

class TestDay33(unittest.TestCase):

    # Day 33: List Intersection
    def test_inter_section(self):
        list1 = [20, 30, 60, 65, 75, 80, 85]
        list2 = [42, 30, 80, 65, 68, 88, 95]
        expected = (80, 65, 30)
        self.assertEqual(inter_section(list1, list2), expected)
        
if __name__ == '__main__':
    unittest.main()