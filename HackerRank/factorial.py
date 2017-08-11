import unittest

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

class TestFactorial(unittest.TestCase):
    def setUp(self):
        pass

    def test_factorial(self):
        num = 5
        result = factorial(num)
        self.assertEqual(result, 120)


if __name__ == "__main__":
    unittest.main()
