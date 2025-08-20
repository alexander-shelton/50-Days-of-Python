#!/usr/bin/env python3
import unittest
from day_41 import words_with_vowels, Car, Ford, BMW, Tesla

class TestDay41(unittest.TestCase):

    # Day 41: Only Words with Vowels
    def test_word_with_vowels(self):
        words = "You have no rhythm,"
        expected = ["you", "have", "no"]
        self.assertEqual(words_with_vowels(words), expected)

    ## Extra Challenge: Class of Cars
    def test_print_cars(self):
        ford1 = Ford('Focus', 'White', 2017, 'Auto', False)
        expected = f"car_model = {ford1.model}\
            \nColor = {ford1.color}\
            \nYear = {ford1.year}\
            \nTranmission = {ford1.transmission}\
            \nElectric = {ford1.electric}"
        self.assertEqual(ford1.print_cars(), expected)
    

if __name__ == '__main__':
    unittest.main()