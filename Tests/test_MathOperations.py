import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))

    def test_MathOperations_sum_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(6, Addition.sum(valuelist))

    def test_MathOperations_diff_list(self):
        sublist = [8,4,2]
        self.assertEqual(2, Subtraction.difference(sublist))


if __name__ == '__main__':
    unittest.main()