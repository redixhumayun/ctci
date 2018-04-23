import unittest
import pdb

class minHeap():
    def __init__(self):
        self._heapList = [0]
        self.size = 0

    @property
    def heapList(self):
        return self._heapList

    def swap(self, parent, child):
        self._heapList[parent], self._heapList[child] = self._heapList[child], self._heapList[parent]

    def percUp(self, i):
        while i // 2 > 0:
            parent = self._heapList[i // 2]
            if self._heapList[i] < parent:
                self.swap(i // 2, i)
            i = i // 2

    def percDown(self, i):
        while i * 2 <= self.size:
            mc = self.minChild(i)
            if self._heapList[i] > self._heapList[mc]:
                self.swap(i, mc)
            i = mc

    def minChild(self, i):
        if (i*2) + 1 > self.size:
            return i * 2
        else:
            left = i * 2
            right = i * 2 + 1
            if self._heapList[left] < self._heapList[right]:
                return left
            else:
                return right

    def insert(self, key):
        self._heapList.append(key)
        self.size += 1
        self.percUp(self.size)

    def delete(self, key):
        index = self.findIndexOfKey(key)
        self._heapList[index] = self._heapList[self.size]
        self._heapList.pop()
        self.size -= 1
        self.percDown(index)

    def findIndexOfKey(self, key):
        for index, value in enumerate(self._heapList):
            if value == key:
                return index

    def getMinimum(self):
        return self._heapList[1] #minHeap so smallest element will always be at root

    def checkForOperation(self, values):
        # pdb.set_trace()
        if values[0] == 1:
            #insertion
            self.insert(values[1])
        if values[0] == 2:
            #deletion
            self.delete(values[1])
        if values[0] == 3:
            #print minimum of all elements in the heap
            return self.getMinimum()

class TestHeap(unittest.TestCase):
    def setUp(self):
        self.heap = minHeap()
        self.heap.checkForOperation([1, 286789035])
        self.heap.checkForOperation([1, 255653921])
        self.heap.checkForOperation([1, 274310529])
        self.heap.checkForOperation([1, 494521015])
        self.heap.checkForOperation([2, 255653921])
        self.heap.checkForOperation([2, 286789035])
        self.heap.checkForOperation([1, 236295092])
        self.heap.checkForOperation([1, 254828111])
        self.heap.checkForOperation([2, 254828111])
        self.heap.checkForOperation([1, 465995753])
        self.heap.checkForOperation([1, 85886315])
        self.heap.checkForOperation([1, 7959587])
        self.heap.checkForOperation([1, 20842598])
        self.heap.checkForOperation([2, 7959587])
        self.heap.checkForOperation([1, -51159108])
        # self.heap.checkForOperation([2, -51159108])
        # self.heap.checkForOperation([1, 7959587])


    def test_getMinimum(self):
        result = self.heap.checkForOperation([3])
        self.assertEqual(result, -51159108)



if __name__ == "__main__":
    unittest.main()
