import unittest
import pdb

class TreeNode():
    '''
    A class for the node of the binary search tree
    '''
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def hasRightChild(self):
        return self.right is not None

    def hasLeftChild(self):
        return self.left is not None

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isLeaf(self):
        return not (self.hasLeftChild() or self.hasRightChild())

    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.right.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                if node.isRightChild():
                    self.parent.right = None #setting to none temporarily
                    succ = self.parent.findSuccessor()
                    self.parent.right = self
        return succ

    def findMin(self):
        if self.left is None:
            return self
        return self.findMin(self.left)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
        else: #node has one child. Only possible case. This child has to be right
        #This is coz we looked for left most node in successor
            node.right.parent = node.parent
            node.parent.left = node.right


    def replaceNodeData(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        if self.hasLeftChild():
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.left:
                    yield elem
            yield self
            if self.hasRightChild():
                for elem in self.right:
                    yield elem

    def __repr__(self):
        return "The key is: %i and the value is: %s" % (self.key, self.value)

class BinarySearchTree():
    '''
    A class for the binary search tree data structure.
    Attributes: root, size
    '''
    def __init__(self):
        self.root = None
        self._size = 0

    @property
    def size(self):
        return self._size

    def put(self, key, val):
        if self.root is None:
            self.root = TreeNode(key, val)
            self._size += 1
        else:
            self._put(key, val, self.root)

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if not currentNode.hasLeftChild():
                currentNode.left = TreeNode(key, val, parent=currentNode)
                self._size += 1
            else:
                self._put(key, val, currentNode.left)
        else:
            if not currentNode.hasRightChild():
                currentNode.right = TreeNode(key, val, parent=currentNode)
                self._size += 1
            else:
                self._put(key, val, currentNode.right)

    def get(self, key):
        if self.root:
            return self._get(key, self.root)
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        if key == currentNode.key:
            return currentNode
        else:
            if key < currentNode.key:
                return self._get(key, currentNode.left)
            else:
                return self._get(key, currentNode.right)
        return None

    def delete(self, key):
        # pdb.set_trace()
        if self._size > 1:
            nodeToRemove = self.get(key)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self._size -= 1
            else:
                raise KeyError('Key not found in tree')
        elif self._size == 1 and key == self.root.key:
            self.root = None
            self._size -= 1
        else:
            raise KeyError('Tree does not contain any keys')

    def remove(self, node):
        if node.isLeaf(): #node is a leaf node
            if node.isLeftChild():
                node.parent.left = None
            elif node.isRightChild():
                node.parent.right = None

        elif node.hasBothChildren():
            #node has both children. It is an internal node
            succ = node.findSuccessor()
            succ.spliceOut() #a method to remove the successor from the tree
            node.key = succ.key
            node.value = succ.value

        else:
            #node has one child.
            if node.hasLeftChild(): #node has a child on the left
                if node.isLeftChild():
                    node.parent.left = node.left
                    node.left.parent = node.parent
                elif node.isRightChild():
                    node.parent.right = node.left
                    node.right.parent = node.parent
                else: #in this case the node is the root
                    node.replaceNodeData(node.left.key, node.left.value,
                                        node.left.left, node.left.right)

            elif node.hasRightChild(): #node has a child on the right
                if node.isLeftChild():
                    node.parent.left = node.right
                    node.right.parent = node.parent
                elif node.isRightChild():
                    node.parent.right = node.right
                    node.right.parent = node.parent
                else:
                    node.replaceNodeData(node.right.key, node.right.value,
                                        node.right.left, node.right.right)

    def __delitem__(self, key):
        self.delete(key)

    def __len__(self):
        return self.size

    def __setitem__(self, key, value):
        self.put(key, value)

    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False


class TestBST(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        array = [(7, 'Hello'), (5, 'World'), (4, 'The'), (11, 'Quick'),
                 (8, 'Brown'), (9, 'Fox'), (6, 'Jumped'), (3, 'Log'), (13, 'Random')]
        for tup in array:
            self.bst.put(tup[0], tup[1])

    def test_put(self):
        self.assertEqual(self.bst.size, 9)
        self.assertEqual(self.bst.root.left.value, 'World')

    def test_setitem(self):
        self.bst[13] = 'Check'
        self.assertEqual(self.bst.root.right.right.right.value, 'Check')

    def test_get(self):
        result = self.bst.get(4)
        self.assertEqual(result.value, 'The')

    def test_contains(self):
        result = 95 in self.bst
        self.assertEqual(result, False)

    def test_deleteLeaf(self):
        self.bst.delete(3)
        result = self.bst.root.left.left.left
        self.assertEqual(result, None)

    def test_deleteOneChild(self):
        self.bst.delete(8)
        result = self.bst.root.right.left
        self.assertEqual(result.key, 9)

    def test_deleteInternalNode(self):
        self.bst.delete(11)
        result = self.bst.root.right
        self.assertEqual(result.key, 13)


if __name__ == "__main__":
    unittest.main()
