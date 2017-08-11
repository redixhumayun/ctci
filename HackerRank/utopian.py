import unittest

def utopian(t, n):
    max_value = max(n)+1
    cache = [0] * (max_value)
    cache[0] = 1
    return_array = []
    for i in range(1, max_value):
        if i % 2 == 0:
            cache[i] = cache[i-1] + 1
        else:
            cache[i] = cache[i-1] * 2

    for numOfCycles in n:
        return_array.append(cache[numOfCycles])
        
    return return_array

class TestUtopian(unittest.TestCase):
    def setUp(self):
        pass

    def testUtopian(self):
        t = 3
        n = [0,1,4]
        result = utopian(t, n)
        self.assertEqual(result, [1, 2, 7])

if __name__ == "__main__":
    unittest.main()
