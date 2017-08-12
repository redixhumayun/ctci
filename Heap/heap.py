import unittest

class Heap():
    '''
    An implementation of the min heap in Python3
    '''
    def __init__(self):
        self._heap = [0]
        self.size = 0

    @property
    def heap(self):
        return self._heap

    def percUp(self, i):
        '''
        A method that will percolate the value up the tree to its current pos
        '''
        while (i // 2) > 0:
            if self._heap[i] < self._heap[i // 2]:
                self._heap[i], self._heap[i // 2] = self._heap[i // 2], self._heap[i]
            i = i // 2

    def insert(self, k):
        self._heap.append(k)
        self.size += 1
        self.percUp(self.size)

    def percDown(self, i):
        while (i * 2) <= self.size:
            mc = self.minChild(i)
            if self._heap[i] > self._heap[mc]:
                self._heap[i], self._heap[mc] = self._heap[mc], self._heap[i]
            i = mc

    def minChild(self, i):
        if (i * 2) + 1 > self.size:
            return i * 2
        else:
            if self._heap[(i*2)+1] < self._heap[i*2]:
                return (i * 2) + 1
            else:
                return i * 2

    def delMin(self):
        valueToDelete = self._heap[1]
        self._heap[1] = self._heap[self.size]
        self.size = self.size - 1
        self.list.pop()
        self.percDown(1)
        return valueToDelete

    def build_heap(self, array):
        i = len(array) // 2
        self.size = len(array)
        self._heap = [0] + array[:]
        while i > 0:
            self.percDown(i)
            i = i - 1

class TestHeap(unittest.TestCase):
    def setUp(self):
        self.heapInst = Heap()
        array = [9, 5, 6, 2, 3]
        self.heapInst.build_heap(array)

    def test_HeapClass(self):
        result = self.heapInst.heap
        self.assertEqual(result, [0,2,3,6,5,9])

    def test_insertElem(self):
        self.heapInst.insert(11)
        result = self.heapInst.heap
        self.assertEqual(result, [0,2,3,6,5,9,11])

if __name__ == "__main__":
    unittest.main()
