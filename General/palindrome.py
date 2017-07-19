import unittest

class HashTable:
    def __init__(self):
        self.size = ord('z') - ord('a') + 1
        self.slots = [None] * self.size
        self.data = [0] * self.size

    def put(self, key, data):
        hashValue = self.hashfunction(key)
        self.slots[hashValue] = key
        self.data[hashValue] += 1

    def get(self, key):
        hashValue = self.hashfunction(key)
        return self.data[hashValue]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)

    def hashfunction(self, value):
        return value % 26


def isPermutationOfPalindrome(string):
    #need to build hash table first
    hashTable = HashTable()

    #populate hash table by going through string
    for index, char in enumerate(string):
        if char != " ":
            hashTable[ord(char.lower())] = 0

    #check hash table to see if string is a palindrome
    return checkHashTable(hashTable)

    #return based on above result

def checkHashTable(hashInstance):
    foundOdd = False
    for i in range(hashInstance.size):
        if hashInstance[i] % 2 == 1:
            if foundOdd:
                return False
            foundOdd = True
    return True

class Testing(unittest.TestCase):
    '''Test Case'''
    data = [('Tact Coa', True)]

    def test_palindrome(self):
        for test_case in self.data:
            expected = isPermutationOfPalindrome(test_case[0])
            self.assertEqual(expected, test_case[1])

if __name__ == "__main__":
    unittest.main()
