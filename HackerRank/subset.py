from collections import defaultdict
import unittest
import pdb

def findSubset(s, n, k):
    # pdb.set_trace()
    remainders = groupByRemainder(s, k)
    count = 0
    for key, value in remainders.items():
        if key == 0:
            count += 1
        else:
            if (k - key) in remainders:
                base = remainders.get(key)
                toCompare = remainders.get(k - key)
                if len(base) > len(toCompare):
                    count += len(base)
                if len(base) == len(toCompare):
                    count += len(base)
                    remainders[k-key] = []
            else:
                count += len(remainders.get(key))

    return count


def groupByRemainder(s, k):
    remainders = defaultdict(list)
    for num in s:
        key = num % k
        remainders[key].append(num)
    return remainders

class TestSubsets(unittest.TestCase):
    def setUp(self):
        pass

    def test_findSubsets(self):
        s = [1,7,2,4]
        n = 3
        k = 3
        result = findSubset(s, n, k)
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
