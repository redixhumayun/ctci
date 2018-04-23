import math
import unittest
import pdb

def power_sum_wrapper(x, n):
    if x == 0:
        return 0
    if isPrime(x):
        if n == x:
            return 1
        else:
            return 0
    else:
        return power_sum(x, n, 1)

def power_sum(x, n, num):
    # pdb.set_trace()
    value = x - (num**n)
    if value < 0:
        return 0
    if value == 0:
        return 0
    else:
        return power_sum(value, n, num+1) + power_sum(x, n, num+1)

def isPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


class TestPowerSum(unittest.TestCase):
    def setUp(self):
        self.x = 10
        self.n = 2

    def test_powerSum(self):
        result = power_sum_wrapper(self.x, self.n)
        self.assertEqual(result, 1)

    def test_isPrime(self):
        result = isPrime(1)
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()
