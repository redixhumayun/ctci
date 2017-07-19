#! /usr/bin/env python3
# from randint import randint
import pdb

class BT():
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def add(self, key, node):
        self.size += 1
        if node is None:
            node = self.root

        if self.root is None:
            self.root = TreeNode(key)
            return

        else:
            if key < node.value:
                node.numLeft += 1
                if node.leftChild is None:
                    node.leftChild = TreeNode(key)
                    return
                else:
                    return self.add(key, node.leftChild)
            else:
                node.numRight += 1
                if node.rightChild is None:
                    node.rightChild = TreeNode(key)
                    return
                else:
                    return self.add(key, node.rightChild)

    def getNode(self, value, root):
        if root is None:
            return
        if value == root.value:
            return root
        elif value < root.value:
            return self.getNode(value, root.leftChild)
        elif value > root.value:
            return self.getNode(value, root.rightChild)

    def print_tree(self, root):
        if root:
            self.print_tree(root.leftChild)
            print(root.value)
            self.print_tree(root.rightChild)

    def countPaths(self, root, pathValue):
        # pdb.set_trace()
        result = 0
        if root is None:
            return 0
        pathsFromRoot = self.sumPath(root, pathValue, 0)
        pathsOnLeft =  self.countPaths(root.leftChild, pathValue)
        pathsOnRight = self.countPaths(root.rightChild, pathValue)

        return pathsFromRoot + pathsOnLeft + pathsOnRight

    def sumPath(self, root, pathValue, result):
        counter = 0
        if root is None:
            return 0

        result += root.value

        if result == pathValue:
            counter += 1

        counter += self.sumPath(root.leftChild, pathValue, result)
        counter += self.sumPath(root.rightChild, pathValue, result)
        return counter




class TreeNode():
    def __init__(self, val, left=None, right=None, numLeft=0, numRight=0):
        self.value = val
        self.leftChild = left
        self.rightChild = right
        self.numLeft = numLeft
        self.numRight = numRight

    def insertLeftChild(self, val):
        self.leftChild = val

    def insertRightChild(self, val):
        self.rightChild = val

    def hasLeftChild(self):
        return self.leftChild is not None

    def hasRightChild(self):
        return self.rightChild is not None

    def hasChildren(self):
        return self.hasLeftChild() and self.hasRightChild()


if __name__ == "__main__":
    # arr = [4,6,7,8,5,9,2,1,3]
    arr = [6,4,9,2,5,1,3,9,7,10,8]
    bt = BT()
    for index, num in enumerate(arr):
        bt.add(num, None)
    result = bt.countPaths2(bt.root, 15)
    print(result)
