import unittest
from stack import Stack

class SortedStack():
    def __init__(self, array):
        self.stack1 = Stack()
        for num in array:
            self.stack1.push(num)
        self.stack2 = Stack()

    def sort(self):
        if self.stack1.isEmpty():
            return
        else:
            elem = self.stack1.pop()
            if self.stack2.isEmpty():
                self.stack2.push(elem)
            else:
                while not self.stack2.isEmpty() and self.comparator(elem, self.stack2.peek()):
                    elem2 = self.stack2.pop()
                    self.stack1.push(elem2)
                self.stack2.push(elem)
        self.sort()

    def rebuildStack(self):
        while not self.stack2.isEmpty():
            elem = self.stack2.pop()
            self.stack1.push(elem)

    def comparator(self, elem, stack2Elem):
        if elem < stack2Elem:
            return True
        else:
            return False

class TestSortedStack(unittest.TestCase):
    def setUp(self):
        array = [7,5,9,11,2,4,3]
        self.sortedStack = SortedStack(array)
        self.sortedStack.sort()

    def test_sort(self):
        result = self.sortedStack.stack2.items
        self.assertEqual(result, [2,3,4,5,7,9,11])

    def test_rebuildStack(self):
        self.sortedStack.rebuildStack()
        result = self.sortedStack.stack1.items
        self.assertEqual(result, [11, 9, 7, 5, 4, 3, 2])


if __name__ == "__main__":
    unittest.main()
