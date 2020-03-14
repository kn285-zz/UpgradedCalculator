import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction
from MathOperations.multiplication import Multiplication
from MathOperations.division import Division
from MathOperations.squareroot import Squareroot
from MathOperations.square import square
from MathOperations.logarithm import Logarithm


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1, 2))

    def test_MathOperations_sum_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(6, Addition.sum(valuelist))

    def test_MathOperations_multiplication(self):
        self.assertEqual(6, Multiplication.multiply(2, 3))

    def test_MathOperations_division(self):
        self.assertEqual(3, Division.divide(9, 3))

    def test_MathOperations_square(self):
        self.assertEqual(81, square.square(9, 2))

    def test_MathOperations_root(self):
        self.assertEqual(3, Squareroot.squareroot(9, 2))

    def test_MathOperations_log(self):
        self.assertEqual(2, Logarithm.log(100, 10))


if __name__ == '__main__':
    unittest.main()
