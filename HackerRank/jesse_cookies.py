import unittest
import pdb

class Heap():
    def __init__(self):
        self._heapList = [0]
        self.size = 0
        self.sizeCopy = 0

    @property
    def heapList(self):
        return self._heapList

    def swap(self, i, j):
        self._heapList[i], self._heapList[j] = self._heapList[j], self._heapList[i]


    def min_heapify(self, i):
        minChild = self.findMinChild(i)
        if i != minChild:
            self.swap(i, minChild)
            self.min_heapify(minChild)

    def findMinChild(self, i):
        smallest = i
        left = i * 2
        right = i * 2 + 1
        if left <= self.size and self._heapList[left] < self._heapList[i]:
            smallest = left
        if right <= self.size and self._heapList[right] < self._heapList[smallest]:
            smallest = right
        return smallest

    def max_heapify(self, i):
        maxChild = self.findMaxChild(i)
        if i != maxChild:
            self.swap(i, maxChild)
            self.max_heapify(maxChild)

    def findMaxChild(self, i):
        largest = 0
        left = i * 2
        right = i * 2 + 1
        if left <= self.size and self._heapList[left] > self._heapList[i]:
            largest = left
        else:
            largest = i
        if right <= self.size and self._heapList[right] > self._heapList[largest]:
            largest = right
        return largest

    def buildHeap(self, array):
        i = len(array) // 2
        self.size = len(array)
        self._heapList = [0] + array[:]
        while i > 0:
            self.max_heapify(i)
            i -= 1

    def heapSort(self):
        self.sizeCopy = self.size

        for index in range(self.size, 0, -1):
            self.swap(1, index)
            self.size -= 1
            self.max_heapify(1)

        self.size = self.sizeCopy #restoring array length after heap sorting

    def delMin(self):
        valueToDelete = self._heapList[1]
        self.swap(1, self.size)
        self._heapList.pop()
        self.size -= 1
        self.min_heapify(1)
        return valueToDelete

    def insert(self, key):
        self._heapList.append(key)
        self.size += 1
        for i in range(self.size // 2, 0, -1):
            self.min_heapify(i)

    def checkWithinLimit(self, limit):
        for i in range(1, self.size + 1, 1):
            if self._heapList[i] < limit:
                return False
        return True


    def findNumberOfOperations(self, limit):
        ctr = 0
        while not checkWithinLimit(limit):
            ctr += 1
            first = self.delMin()
            second = self.delMin()
            result = first * 1 + second * 2
            self.insert(result)
            self.heapSort()




class TestHeap(unittest.TestCase):
    def setUp(self):
        array = [1, 2, 3, 9, 10, 12]
        self.heap = Heap()
        self.heap.buildHeap(array)
        self.heap.heapSort()

    def test_heapSort(self):
        result = self.heap.heapList
        self.assertEqual(result, [0, 1, 2, 3, 9, 10, 12])

    def test_delMin(self):
        valueToDelete = self.heap.delMin()
        result = self.heap.heapList
        self.heap.heapSort()
        self.assertEqual(result, [0, 2, 9, 3, 12, 10])


if __name__ == "__main__":
    unittest.main()
