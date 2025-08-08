#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_5 import my_discount, count_student_gender

class TestDay5(unittest.TestCase):

    # Day 5: My Discount
    def test_my_discount(self):
        with patch('builtins.input', side_effect=['150', '15']):
            result = my_discount()
            self.assertEqual(result, 127.5)

    # Extra Challenge: Tuple of Student Sex
    def test_count_student_gender(self):
        students = [
            'Male', 'Female', 'female', 'male', 'male', 'male', 
            'female', 'male', 'Female', 'Male', 'Female', 'Male', 
            'female'
        ]
        expected = [("Male", 7), ("Female", 6)]
        self.assertEqual(count_student_gender(students), expected)

if __name__ == '__main__':
    unittest.main()