#!/usr/bin/env python3
import unittest
from day_47 import save_json, read_json

class TestDay47(unittest.TestCase):

    # Day 47: Save a JSON
    def test_save_json(self):
        names = {'name': 'Carol', 'sex': 'female', 'age': 55}
        result = save_json(names)
        self.assertEqual(result, "Names saved to 'names.json'")


    ## Read JSON
    def test_read_json(self):
        names = {'name': 'Carol', 'sex': 'female', 'age': 55}
        self.assertEqual(read_json(), names)

if __name__ == '__main__':
    unittest.main()