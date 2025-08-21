#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_43 import student_marks

class TestDay43(unittest.TestCase):

    # Day 43: Student Marks
    def test_student_marks(self):
        with patch('builtins.input', side_effect=['Alex', '100','Bethany', '90', 'Carl', '85', 'alex', '95', 'Don', '60', 'Frank', '50', 'done']):
            result = student_marks()
            expected = {'alex': [100, 95], 'bethany': [90], 'carl': [85], 'don': [60], 'frank': [50]}
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()