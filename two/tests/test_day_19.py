#!/usr/bin/env python3
import unittest
from day_19 import count_words, count_elements

class TestDay19(unittest.TestCase):
    words = "I love learning"

    # Day 19: Count Words
    def test_count_words(self):
        self.assertEqual(count_words(self.words), 3)

    ## Extra Challenge: Count Elements
    def test_count_elements(self):
        self.assertEqual(count_elements(self.words), 13)
    
if __name__ == "__main__":
    unittest.main()