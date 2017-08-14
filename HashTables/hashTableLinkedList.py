import hashlib
import unittest

class Node():
    '''
    A class for the node to be used in the linked list
    '''
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        print(self.value)

    def __repr__(self):
        print(self.value)

class LinkedList():
    '''
    A linked list class to be used for chaining in hash tables
    '''
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addNode(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def removeNode(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                if current.prev is not None: #check if not the head
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else: #if node is head
                    current.next.prev = None
                    self.head = current.next
                self.size -= 1
                return current.value
            current = current.next
        return -1

    def findNode(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current.value
            current = current.next
        return -1 #node not found

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next


class HashTable():
    '''
    A class describing a hash table. Maps strings onto a hash table
    '''
    def __init__(self, size):
        self._hashList = [LinkedList()] * size
        self.size = size

    @property
    def hashList(self):
        return self._hashList

    def addItem(self, string):
        '''
        A function to add the string to a hash table
        '''
        generatedHash = self.hash(string)
        self._hashList[generatedHash].addNode(string)

    def hash(self, string):
        return hashlib.md5(string.encode('UTF-8')).digest()[0] % self.size

    def findItem(self, string):
        generatedHash = self.hash(string)
        result = self._hashList[generatedHash].findNode(string)
        return result

    def deleteItem(self, string):
        generatedHash = self.hash(string)
        return self._hashList[generatedHash].removeNode(string)

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

    def test_findItem(self):
        string = 'Hello World'
        result = self.hashInst.findItem(string)
        self.assertEqual(result, 'Hello World')

    def test_deleteItem(self):
        string = 'Hello World'
        result = self.hashInst.deleteItem(string)
        self.assertEqual(result, 'Hello World')

    def test_findItemForNone(self):
        string = 'Not in this list'
        result = self.hashInst.findItem(string)
        self.assertEqual(result, -1)

    def test_LinkedListInstance(self):
        result = self.hashInst.hashList[7]
        self.assertEqual(True, isinstance(result, LinkedList))

    def test_writingFile(self):
        with open('./strings.txt', 'r') as myfile:
            data = myfile.readlines()
            for line in data:
                line.replace('\n', '')
                self.hashInst.addItem(line)

        result = self.hashInst.findItem('Easier said than done')
        print(result)

if __name__ == "__main__":
    unittest.main()
