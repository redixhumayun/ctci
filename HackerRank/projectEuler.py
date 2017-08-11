import unittest
import pdb
from fractions import Fraction

def findSumOfProducts(number):
    result = 0
    for num in range(5, number + 1):
        pdb.set_trace()
        result += findMaxProduct(num)
    return result

def findMaxProduct(n):
    max_value = 0
    for divisor in range(1, n):
        product = Fraction(n**divisor, divisor**divisor)
        if product > max_value:
            max_value = product
    return isTerminating(max_value.numerator, max_value.denominator)

def isTerminating(num, den):
    numCopy = num
    denCopy = den
    while den % 2 == 0:
        den = den / 2
    while den % 5 == 0:
        den = den / 5
    return (-1 * (numCopy / denCopy)) if den == 1 else (numCopy / denCopy)


class TestProjectEuler(unittest.TestCase):
    def setUp(self):
        pass

    def test_isTerminatingPos(self):
        num = 2
        den = 3
        result = isTerminating(num, den)
        self.assertEqual(result, 0.6666666666666666)

    def test_isTerminatingNeg(self):
        num = 5
        den = 2
        result = isTerminating(num, den)
        self.assertEqual(result, -2.5)

    def test_findMaxProduct(self):
        num = 8
        result = findMaxProduct(num)
        self.assertEqual(round(result, 9), 18.962962963)

    def test_findSumOfProducts(self):
        number = 100
        result = findSumOfProducts(number)
        self.assertEqual(result, 2438)

if __name__ == "__main__":
    unittest.main()
