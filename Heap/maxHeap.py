import unittest
import pdb

class Heap():
    '''
    A class to re-create a max heap
    '''
    def __init__(self):
        self._heapList = [0] #0 is so that integer division can be used
        self.size = 0

    @property
    def heapList(self):
        return self._heapList

    def maxHeapify(self, i):
        if i * 2 > self.size:
            return
        mc = self.maxChild(i)
        if self._heapList[i] < self._heapList[mc]:
            self._heapList[i], self._heapList[mc] = self._heapList[mc], self._heapList[i]
            self.maxHeapify(mc)
        return

    def maxChild(self, i):
        if (i * 2) + 1 > self.size:
            return i * 2
        else:
            left = i * 2
            right = (i * 2) + 1
            if self._heapList[left] > self._heapList[right]:
                return left
            else:
                return right

    def build_heap(self, array):
        i = len(array) // 2
        self._heapList = [0] + array[:] #0 is so that integer div can be used
        self.size = len(array)
        for index in range(i, 0, -1):
            self.maxHeapify(index)

    def heap_sort(self):
        for index in range(self.size, 1, -1):
            self._heapList[1], self._heapList[index] = self._heapList[index], self._heapList[1]
            self.size -= 1
            self.maxHeapify(1)

    def insert(self, k):
        self._heapList.append(k)
        self.size += 1
        for index in range((self.size // 2), 0, -1):
            self.maxHeapify(index)


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.heap = Heap()
        arr = [1,2,3,4,5,6]
        self.heap.build_heap(arr)

    def test_buildHeap(self):
        result = self.heap.heapList
        self.assertEqual(result, [0,6,5,3,4,2,1])

    def test_heapSort(self):
        self.heap.heap_sort()
        heapSortedArray = self.heap.heapList
        self.assertEqual(heapSortedArray, [0,1,2,3,4,5,6])

    def test_insert(self):
        self.heap.insert(8)
        result = self.heap.heapList
        self.assertEqual(result, [0, 8, 5, 6, 4, 2, 1, 3])

if __name__ == "__main__":
    unittest.main()
