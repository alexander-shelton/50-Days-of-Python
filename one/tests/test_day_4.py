#!/usr/bin/env python3
import unittest
from day_4 import only_floats, word_index

class TestDay4(unittest.TestCase):

    # Day 4: Only Floats
    def test_only_floats(self):
        self.assertEqual(only_floats(12.1, 1.4), 2)
        self.assertEqual(only_floats(12.1, 23), 1)
        self.assertEqual(only_floats(12, 23), 0)

    # Extra Challenge: Index of the Longest Word
    def test_word_index(self):
        words1 = ["Hate", "remorse", "vengeance"]
        self.assertEqual(word_index(words1), 2)
        words2 = ["Love", "Hate"]
        self.assertEqual(word_index(words2), 0)

if __name__ == '__main__':
    unittest.main()