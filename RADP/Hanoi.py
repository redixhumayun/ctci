#! /usr/bin/env python3

class Stack():
    '''
    A class for a stack
    '''
    def __init__(self, value):
        self.value = value
        self.stack = []

    def add(self, value):
        self.stack.append(value)

    def popElem(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def __str__(self):
        return self.value

def Hanoi(num, stackSrc, stackDest, stackTemp):
    if num == 1:
        disk = stackSrc.popElem() #get last element from stack

        print("Moving " + str(num) + " from ", end="")
        print(stackSrc, end="")
        print(" to ", end="")
        print(stackDest)

        stackDest.add(num)
    else:
        Hanoi(num - 1, stackSrc, stackTemp, stackDest)
        #moving disk from src to dest
        disk = stackSrc.popElem()

        print("Moving " + str(num) + " from ", end="")
        print(stackSrc, end="")
        print(" to ", end="")
        print(stackDest)
        
        stackDest.add(disk)
        #end of moving from src to dest
        Hanoi(num - 1, stackTemp, stackDest, stackSrc)

if __name__ == "__main__":
    stackA = Stack('A')
    for i in range(1, 4, 1):
        stackA.add(i)
    stackB = Stack('B')
    stackC = Stack('C')
    Hanoi(3, stackA, stackB, stackC)
