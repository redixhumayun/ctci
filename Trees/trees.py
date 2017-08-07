#! /usr/bin/env python3
import sys
import pdb as p

class BT():
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def add(self, key, node):
        # p.set_trace()
        if node is None:
            node = self.root

        if self.root is None:
            self.root = TreeNode(key)
            return

        else:
            if key <= node.value:
                if node.leftChild is None:
                    node.leftChild = TreeNode(key)
                    return
                else:
                    return self.add(key, node.leftChild)
            else:
                if node.rightChild is None:
                    node.rightChild = TreeNode(key)
                    return
                else:
                    return self.add(key, node.rightChild)

    def getNode(self, value, root):
        if root is None:
            return
        if root.value == value:
            return root
        foundNode = self.getNode(value, root.leftChild)
        if foundNode is None:
            foundNode = self.getNode(value, root.rightChild)
        return foundNode

    def print_tree(self, root):
        # p.set_trace()
        if root:
            self.print_tree(root.leftChild)
            print(root.value)
            self.print_tree(root.rightChild)

    def recurseTree(self, root):
        weaved = []
        if not root.hasChildren():
            return [root.value]
        else:
            prefix = []
            prefix.append(root.value)
            res1 = self.recurseTree(root.leftChild)
            res2 = self.recurseTree(root.rightChild)
            self.permuteArray(res1, res2, prefix, weaved)

    def permuteArray(self, arr1, arr2, prefix, weaved):
        p.set_trace()
        if len(arr1) == 0 or len(arr2) == 0:
            #base case
            res = list(prefix)
            res.extend(arr1)
            res.extend(arr2)
            weaved.append(res)
            return
        firstHead = arr1.pop(0)
        prefix.append(firstHead)
        self.permuteArray(arr1, arr2, prefix, weaved)
        prefix.pop()
        arr1.insert(0, firstHead)

        secondHead = arr2.pop(0)
        prefix.append(secondHead)
        self.permuteArray(arr1, arr2, prefix, weaved)
        prefix.pop()
        arr2.insert(0, secondHead)



class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.leftChild = left
        self.rightChild = right

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
    arr = [1,2,4,5,6,7]
    bt = BT()
    for index, num in enumerate(arr):
        bt.add(num, None)
    nodeToFind = bt.getNode(9, bt.root)
    mainNode = bt.getNode(1, bt.root)
    # bt.print_tree(bt.root)
    print(bt.root.rightChild.value)
