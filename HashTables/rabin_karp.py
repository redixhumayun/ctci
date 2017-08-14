import unittest

def rabin_karp(pattern, text, q):
        m = len(pattern)
        n = len(text)
        d = 256
        h = pow(d, m-1) % q #what does this line do? 
        p = 0
        t = 0
        result = []

        for i in range(m): #calculate hash for pattern and substring from text of length m
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q
        for i in range(n-m+1):
            if p == t:
                for j in range(m):
                    if pattern[j] != text[i+j]:
                        break
                else:
                    result.append(i)
            if i < n - m:
                t = (t - h*ord(text[i]))%q #remove first letter
                t = (t + h*ord(text[i+m]))%q #add first letter after pattern
                t = (t+q) % q
        return result

class TestRobinKarp(unittest.TestCase):
    def setUp(self):
        pass

    def test_pass(self):
        self.text = 'doe are hearing me'
        self.pattern = 'ear'
        result = rabin_karp(self.pattern, self.text, 11)
        self.assertEqual(result, [])

    def test_pass_2(self):
        self.text = 'The quick brown fox jumped over the log'
        self.pattern = 'fox'
        result = rabin_karp(self.pattern, self.text, 17)
        self.assertEqual(result, [16])


if __name__ == "__main__":
    unittest.main()
