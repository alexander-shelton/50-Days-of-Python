#!/usr/bin/env python3
import unittest
from day_8 import odd_even, prime_numbers

class TestDay8(unittest.TestCase):

    # Day 8: Odd and Even
    def test_odd_even(self):
        nums = [1, 2, 3, 4, 6]
        self.assertEqual(odd_even(nums), 5)

    # Extra Challenge: List of Prime Numbers
    def test_prime_numbers(self):
        num = 10
        expected = [2, 3, 5, 7]
        self.assertEqual(prime_numbers(10), expected)

if __name__ == '__main__':
    unittest.main()