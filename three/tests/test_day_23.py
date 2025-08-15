#!/usr/bin/env python3
import unittest
from day_23 import Calculator, multiply_words

class TestDay23(unittest.TestCase):

    # Day 23: Simple Calculator
    def test_add(self):
        #self.calculator = Calculator
        num1 = 1
        num2 = 4
        expected = 5
        #self.assertEqual(self.calculator.add(num1, num1), expected)

    def test_subtract(self):
        num1 = 4
        num2 = 1
        expected = 3
        #self.assertEqual(self.calculator.subtract(num1, num1), expected)
        
    def test_divide(self):
        num1 = 10
        num2 = 2
        expected = 5
        #self.assertEqual(self.calculator.divide(num1, num1), expected)

    def test_multiply(self):
        num1 = 5
        num2 = 1
        expected = 5
        #self.assertEqual(self.calculator.add(num1, num1), expected)

    def test_multiply_words(self):
        string = "love live and laugh"
        expected = "240: love (4), live (4), and (3), laugh (5)"
        #self.assertEqual(multiply_words(string), expected)
        string = "Hate war love Peace"
        expected = "12 – war ( 3) love ( 4)"
        #self.assertEqual(multiply_words(string), expected)

if __name__ == '__main__':
    unittest.main()