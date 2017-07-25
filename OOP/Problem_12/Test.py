#! /usr/bin/env python3
from HashTable import HashTable

class Test():
    '''
    A class for testing out the hash table
    '''

    def __init__(self):
        self.hashTable = HashTable()
        self.passwords = ['united58', 'United58', 'ManUnited!*58', 'United!*58']

        for password in self.passwords:
            hashValue = self.hashTable.hashInput(password)
            self.hashTable.addToArray(hashValue, password)

        self.lookForHash('united58')

    def lookForHash(self, userInput):
        self.hashTable.checkForHash(userInput)

if __name__ == "__main__":
    test = Test()
