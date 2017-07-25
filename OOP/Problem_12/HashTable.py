#! /usr/bin/env python3
from LinkedList import LinkedList
import warnings

class HashTable():
    '''
    A class for the hash table
    Attributes: hashedArray
    '''
    linkedList = LinkedList()

    def __init__(self):
        self.hashedArray = [self.linkedList] * 8

    def hashInput(self, userInput):
        return abs(hash(userInput)) % (10**8) % 8
        #10**8 to grab last eight digits and 8 to fit into array of size 8

    def addToArray(self, hashValue, userInput):
        if self.detectDuplicate(hashValue, userInput):
            # raise ValueError("Duplicate detected")
            warnings.warn("Duplicate detected")
        else:
            self.hashedArray[hashValue].addNode(userInput)

    def getValue(self, userInput):
        hashValue = self.hashInput(userInput)

    def removeFromArray(self, userInput):
        hashValue = self.hashInput(userInput)
        self.hashedArray[hashValue].deleteNode(userInput)

    def checkForHash(self, userInput):
        #method to check if hash already exists
        hashValue = self.hashInput(userInput)
        if self.hashedArray[hashValue].searchNode(userInput):
            print("Yes, this hash already exists")
        else:
            print("Sorry, this hash is not stored on the system")

    def detectDuplicate(self, hashValue, userInput):
        result = self.hashedArray[hashValue].searchNode(userInput)
        if result is not None:
            return True
        else:
            return False
