import unittest
from collections import deque

class Queue():
    def __init__(self):
        self.queue = deque([], 10)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft()

    def peek(self):
        return self.queue[0]

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()
        self.q.enqueue(2)

    def test_enqueue(self):
        result = self.q.peek()
        self.assertEqual(result, 2)

    def test_dequeue(self):
        result = self.q.dequeue()
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()
