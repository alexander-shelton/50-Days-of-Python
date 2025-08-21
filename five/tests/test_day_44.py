#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from day_44 import save_emails, open_emails

class TestDay44(unittest.TestCase):

    # Day 44: Save Emails
    def test_save_emails(self):
        with patch('builtins.input', side_effect=['jj@gmail.com', 'kate@yahoo.com', 'alex@gmail.com', 'done']):
            result = save_emails()
            expected = "Emails saved to file 'emails.csv'"
            self.assertEqual(result, expected)

    def test_open_emails(self):
        result = open_emails()
        expected = ['jj@gmail.com', 'kate@yahoo.com']
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()