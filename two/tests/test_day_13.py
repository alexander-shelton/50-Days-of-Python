#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_13 import your_vat, python_snakes
class TestDay13(unittest.TestCase):

    # Day 13: Your VAT
    def test_your_vat(self):
        with patch('builtins.input', side_effect=[220, 15]):
            result = your_vat()
            expected = 253
            self.assertEqual(result, expected)

    ## Extra Challenge: Python Snakes
    def test_python_snakes(self):
        pass

        
if __name__ == "__main__":
    unittest.main()