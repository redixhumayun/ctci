import unittest

def designer(h, word):
    maximum = 0
    for char in word:
        if h[ord(char) - 97] > maximum:
            maximum = h[ord(char) - 97]

    return maximum * len(word)


class TestDesigner(unittest.TestCase):
    def setUp(self):
        pass

    def testDesigner(self):
        h = [i for i in range(26)]
        word = 'abc'
        result = designer(h, word)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()
