import unittest

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
        return self.right

    def hasLeftChild(self):
        return self.left

    def isLeaf(self):
        return self.hasLeftChild() or self.hasRightChild()

    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

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
                currentNode.left = TreeNode(key, val)
                self._size += 1
            else:
                self._put(key, val, currentNode.left)
        else:
            if not currentNode.hasRightChild():
                currentNode.right = TreeNode(key, val)
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

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

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
                 (8, 'Brown'), (9, 'Fox'), (6, 'Jumped'), (3, 'Log')]
        for tup in array:
            self.bst.put(tup[0], tup[1])

    def test_put(self):
        self.assertEqual(self.bst.size, 8)
        self.assertEqual(self.bst.root.left.value, 'World')

    def test_setitem(self):
        self.bst[13] = 'Check'
        self.assertEqual(self.bst.root.right.right.value, 'Check')

    def test_get(self):
        result = self.bst.get(4)
        self.assertEqual(result.value, 'The')

    def test_contains(self):
        result = 95 in self.bst
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()
