#! /user/bin/env python3
class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        try:
            return self.items[-1]
        except ValueError:
            print("Empty queue")

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeueAny(self):
        return self.items.pop()

    def dequeueDog(self):
        while not self.isEmpty():
            elem = self.dequeueAny()
            if elem.type is 'dog':
                return elem
        raise ValueError('No dogs at this time')

    def dequeueCat(self):
        while not self.isEmpty():
            elem = self.dequeueAny()
            if elem.type is 'cat':
                return elem
        raise ValueError('No cats at this time')


class Node():
    def __init__(self, name, type):
        self.name = name
        self.type = type


l = [('Roger', 'dog'), ('Jeeves', 'cat'), ('mofo', 'cat'), ('Naina', 'dog'), ('Duke', 'dog')]
myQ = Queue()
for animal in l:
    node = Node(animal[0], animal[1])
    myQ.enqueue(node)

print(myQ.dequeueCat().name)
