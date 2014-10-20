import unittest

from week0_day2 import *


class Testsandstuff(unittest.TestCase):

    def test_count(self):
        self.assertEqual({'apple': 2, 'pie': 1, 'banana': 1}, count_words(
            ["apple", "banana", "apple", "pie"]))

    def test_count_again(self):
        self.assertEqual({}, count_words([]))

    def test_count_againandagain(self):
        self.assertEqual({'asd': 4}, count_words(['asd', 'asd', 'asd', 'asd']))

    def test_count_againandagainandagain(self):
        self.assertEqual({}, count_words(["    "]))

    def test_unique_words_count(self):
        self.assertEqual(0, unique_words_count([]))

    def test_unique_words_count_again(self):
        self.assertEqual(
            3, unique_words_count(['asd', 'dsa', 'slkhnsdlkf', 'asd']))

    def test_unique_words_count_again_again(self):
        self.assertEqual(0, unique_words_count(["   "]))

    def test_groupby(self):
        self.assertEqual({0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}, groupby(
            lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))

    def test_groupby_again(self):
        self.assertEqual({"same": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}, groupby(
            lambda x: "same", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_prepare_meal(self):
        self.assertEqual("", prepare_meal(0))

    def test_reduce_file_path(self):
        self.assertEqual("/", reduce_file_path("///////"))

    def test_sort_fractions(self):
        self.assertEqual([(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]
, sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))

if __name__ == '__main__':
    unittest.main()
