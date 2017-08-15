import unittest
from stack import Stack
import pdb

class SetOfStacks():
    def __init__(self):
         self.set = [0] * 3
         self.index = 0
         self.set[self.index] = Stack()

    def returnStackAtIndex(self, i):
        return self.set[i]

    def push(self, value):
        # pdb.set_trace()
        if not isinstance(self.set[self.index], Stack):
            self.set[self.index] = Stack()

        if self.set[self.index].size <= self.set[self.index].maxSize:
            self.set[self.index].push(value)
        else:
            self.index += 1
            self.push(value)

    def pop(self):
        if self.set[self.index].size == 0:
            self.set[self.index] = 0
            self.index -= 1
            return self.pop()
        else:
            return self.set[self.index].pop()

    def peek(self):
        if self.set[self.index].size == 0:
            self.index -= 1
            return self.peek()
        else:
            return self.set[self.index].peek()

    def isEmpty(self):
        return self.set[self.index].size == 0

class TestSetOfStacks(unittest.TestCase):
    def setUp(self):
        self.sos = SetOfStacks()

    def test_push(self):
        for i in range(3):
            self.sos.push(i)
        self.assertEqual(self.sos.returnStackAtIndex(0).size, 3)

    def test_shiftOverToNewStack(self):
        for i in range(8):
            self.sos.push(i)
        self.assertEqual(self.sos.returnStackAtIndex(1).size, 2)

    def test_removeFromNewStack(self):
        for i in range(7):
            self.sos.push(i)
        self.sos.pop()
        result = self.sos.pop()
        self.assertEqual(result, 5)

    def test_peekAtPrevStack(self):
        for i in range(7):
            self.sos.push(i)
        self.sos.pop()
        self.assertEqual(self.sos.peek(), 5)

if __name__ == "__main__":
    unittest.main()
