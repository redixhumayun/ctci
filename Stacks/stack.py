import unittest

class Stack():
    '''
    A class for the stack data structure
    '''

    def __init__(self):
        self._items = []
        self.size = 0
        self.maxSize = 5

    @property
    def items(self):
        return self._items

    def push(self, item):
        self._items.append(item)
        self.size += 1

    def pop(self):
        try:
            result = self._items.pop()
        except IndexError:
            return -1
        self.size -= 1
        return result

    def peek(self):
        try:
            return self._items[-1]
        except IndexError:
            return -1

    def isEmpty(self):
        return self.size == 0

    def __repr__(self):
        return str(self.items)


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_addItem(self):
        self.stack.push(2)
        self.assertEqual(self.stack.size, 1)

    def test_popItem(self):
        result = self.stack.pop()
        self.assertEqual(result, -1)

    def test_isEmpty(self):
        self.assertEqual(self.stack.isEmpty(), True)

if __name__ == "__main__":
    unittest.main()
