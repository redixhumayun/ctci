import unittest

def hurdle(n, k, height):
    maximum = 0
    for h in height:
        if h > maximum:
            maximum = h
    return (maximum - k) if maximum > k else 0


class TestHurdle(unittest.TestCase):
    def setUp(self):
        pass

    def test_hurdle(self):
        n = 5
        k = 4
        height = [1,6,3,5,2]
        result = hurdle(n, k, height)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()
