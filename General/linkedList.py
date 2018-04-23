class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next

#Implementing a stack here
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, k):
        size = self.size()
        count = 0
        current = self.head
        while current:
            if count == k:
                return current
            count += 1
            current = current.get_next()

    def generate(self, data):
        for i in data:
            self.insert(i)
        return

    def print_data(self):
        current = self.head
        while current:
            print(current.data)
            current = current.get_next()
        return

    #Reverses the linked list iteratively
    def reverse(self):
        current = self.head
        prev = None
        while current:
            n = Node(current.data)
            n.set_next(prev)
            prev = n
            current = current.get_next()
        return n

    #Reverses the linked list recursively
    def reverse_recur(self, current):
        # print("Current: ", current.data)
        if current.get_next() is None:
            self.head = current
            return

        n = current.get_next()
        current.set_next(prev)
        self.reverse_recur(n, current)
        return self

    def loopDetection(self):
        fast = self.head
        slow = self.head
        ctr = 0

        while fast and slow:
            slow = slow.get_next()
            fast = fast.get_next().get_next()
            ctr += 1
            if fast is slow:
                print("Intersection found")
                self.getIntersection(ctr)




linkedList = LinkedList()
#linkedList.generate([1,2,3,4,5,6])
linkedList.generate(['a', 'm', 'm', 'a'])
result = linkedList.isPalindrome()
print(result)
