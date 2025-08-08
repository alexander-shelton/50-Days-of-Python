#!/usr/bin/env python3
import unittest
from day_7 import string_range, names_starting_with_letter

class TestDay7(unittest.TestCase):
    # Day 7: String Range
    def test_string_range(self):
        num = 6
        expected = "0.1.2.3.4.5"
        self.assertEqual(string_range(6), expected)
    
    # Extra Challenge: Dictionary of Names
    def test_names_starting_with_letter(self):
        names = [
            "Joseph", "Nathan", "Sasha", "Kelly", 
            "Muhammad", "Jabulani", "Sera", "Patel", "Sera"
        ] 
        expected = {"Sasha": 1, "Sera": 2}
        self.assertEqual(names_starting_with_letter(names, 's'), expected)
        expected = {"Nathan": 1}
        self.assertEqual(names_starting_with_letter(names, 'n'), expected)

if __name__ == '__main__':
    unittest.main()