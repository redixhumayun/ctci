import hashlib
import unittest


class HashTable():
    '''
    A class describing a hash table. Maps strings onto a hash table
    '''
    def __init__(self, size):
        self._hashList = [0] * size
        self.size = size
        self._entries = 0

    @property
    def hashList(self):
        return self._hashList

    @property
    def entries(self):
        return self._entries

    def addItem(self, string):
        '''
        A function to add the string to a hash table
        '''
        generatedHash = self.hash(string)
        if self._hashList[generatedHash] == 0:
            self._hashList[generatedHash] = string
            self._entries += 1


    def hash(self, string):
        return hashlib.md5(string.encode('UTF-8')).digest()[0] % self.size

    def findItem(self, string):
        generatedHash = self.hash(string)
        result = self._hashList[generatedHash]
        if result == 0:
            return -1
        else:
            return result

    def deleteItem(self, string):
        generatedHash = self.hash(string)
        if self._hashList[generatedHash] == 0:
            return -1
        else:
            self._entries -= 1
            return self._hashList.pop(generatedHash)

    def __iter__(self):
        for data in self.hashList:
            yield data


class TestHashClass(unittest.TestCase):
    def setUp(self):
        self.hashInst = HashTable(19)
        string = 'Hello World'
        string2 = 'Goodbye World'
        self.hashInst.addItem(string)
        self.hashInst.addItem(string2)

    def test_addItem(self):
        noOfEntries = self.hashInst.entries
        self.assertEqual(noOfEntries, 2)

    def test_findItem(self):
        string = 'Hello World'
        result = self.hashInst.findItem(string)
        self.assertEqual(result, 'Hello World')

    def test_deleteItem(self):
        string = 'Hello World'
        result = self.hashInst.deleteItem(string)
        self.assertEqual(result, 'Hello World')



if __name__ == "__main__":
    unittest.main()
