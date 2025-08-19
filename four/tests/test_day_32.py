#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_32 import password_validator, email_validator

class TestDay32(unittest.TestCase):

    # Day 32: Password Validator
    def test_password_validator(self):
        with patch("builtins.input", side_effect=['ValidPassword1']):
            result = password_validator()
            expected = 'ValidPassword1'
            self.assertEqual(result, expected)

    ## Extra Challenge: Valid Email
    def test_email_validator(self):
        emails = [ "ben@mail.com", "john@mail.cm", "kenny@gmail.com", "@list.com" ]
        expected = ['ben@mail.com', 'kenny@gmail.com']
        self.assertEqual(email_validator(emails), expected)
        emails = [ "ben@mail.", "john@mail.cm", "kenny@.com", "@list.com" ]
        expected = "All emails are invalid."
        self.assertEqual(email_validator(emails), expected)

if __name__ == '__main__':
    unittest.main()