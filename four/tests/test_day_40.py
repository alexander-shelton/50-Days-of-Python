#!/usr/bin/env python3
import unittest
from day_40 import translate

class TestDay40(unittest.TestCase):

    # Day 40: Pig Latin
    def test_translate(self):
        my_string = "i love python"
        expected = "iyay ovelay ythonpay"
        self.assertEqual(translate(my_string), expected)

if __name__ == '__main__':
    unittest.main()