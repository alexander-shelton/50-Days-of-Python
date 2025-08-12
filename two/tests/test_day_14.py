#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_14 import flat_list, your_salary

class TestDay14(unittest.TestCase):

    # Day 14: Flat List
    def test_flat_list(self):
        nested_list = [[1, 2, 3], [4, 5], [6]]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(flat_list(nested_list), expected)

    # Day 14: Your Salary
    def test_your_salary(self):
        with patch('builtins.input', side_effect=["John Kelly", 105, 20]):
            result = your_salary()
            expected = "Teacher: John Kelly\nPeriods: 105\nGross salary: 2,125"
            self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()