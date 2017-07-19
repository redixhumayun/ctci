class Stack():
    def __init__(self):
        self.mainStack = []
        self.tempStack = []

    def push(self, stack, item):
        stack.append(item)

    def pop(self, stack):
        return stack.pop()

    def peek(self, stack):
        return stack[-1]

    def size(self, stack):
        return len(stack)

    def isEmpty(self, stack):
        return self.size(stack) == 0

    def sort(self):
        while self.size(self.mainStack) > 0:
            print("********")
            elem = self.pop(self.mainStack)
            print("elem: ", elem)
            if self.isEmpty(self.tempStack):
                self.push(self.tempStack, elem)
            else:
                if elem < self.peek(self.tempStack):
                    print("first if statement")
                    print("elem: ", elem)
                    self.push(self.mainStack, self.pop(self.tempStack))
                    self.push(self.tempStack, elem)
                else:
                    print("second if statement")
                    print("elem: ", elem)
                    self.push(self.tempStack, elem)

    def printStack(self):
        for i in range(self.size(self.tempStack)):
            print(self.pop(self.tempStack))

arr = [4,3,5,1,2]
stack = Stack()

for i in arr:
    stack.push(stack.mainStack, i)

stack.sort()
stack.printStack()
