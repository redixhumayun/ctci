import unittest
from BST import TreeNode
from BST import BinarySearchTree
import pdb

class AVLNode(TreeNode):
    '''
    A class for the AVL tree node. Inherits from TreeNode class
    '''
    def __init__(self, key, value, left=None, right=None, parent=None, balanceFactor=0):
        super().__init__(key, value, left, right, parent)
        self.balanceFactor = balanceFactor

class AVL(BinarySearchTree):
    '''
    A class for the AVL tree. Inherits from the BST class
    '''
    def __init__(self):
        super().__init__()

    def _put(self, key, value, currentNode):
        if key < currentNode.key:
            if not currentNode.hasLeftChild():
                currentNode.left = AVLNode(key, value, parent=currentNode,
                                            balanceFactor=0)
                self._size += 1
                self.updateBalance(currentNode.left)
            else:
                self._put(key, value, currentNode.left)
        else:
            if not currentNode.hasRightChild():
                currentNode.right = AVLNode(key, value, parent=currentNode,
                                            balanceFactor=0)
                self._size += 1
                self.updateBalance(currentNode.right)
            else:
                self._put(key, value, currentNode.right)

    def put(self, key, value):
        pdb.set_trace()
        if self.root is None:
            self.root = AVLNode(key, value)
            self._size += 1
        else:
            self._put(key, value, self.root)

    def updateBalance(self, node):
        '''
        This method is used to update the balance of each node
        '''
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
        else:
            if node.parent is not None:
                if node.isLeftChild():
                    node.parent.balanceFactor += 1
                else:
                    node.parent.balanceFactor -= 1
                if node.parent.balanceFactor != 0:
                    self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):
            #do a left rotation about the node
            newRoot = rotRoot.right
            rotRoot.right = newRoot.left
            if newRoot.left is not None:
                newRoot.left.parent = rotRoot
            newRoot.parent = rotRoot.parent
            if rotRoot == self.root:
                self.root = newRoot
            else:
                if rotRoot.isLeftChild():
                    rotRoot.parent.left = newRoot
                else:
                    rotRoot.parent.right = newRoot
            newRoot.left = rotRoot
            rotRoot.parent = newRoot
            rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
            newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot):
        #do a right rotation about the node
        newRoot = rotRoot.left
        rotRoot.left = newRoot.right
        if newRoot.right is not None:
            newRoot.right.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot == self.root:
            newRoot = self.root
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.left = newRoot
            else:
                rotRoot.parent.right = newRoot
        newRoot.right = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.right and node.right.balanceFactor > 0:
                self.rotateRight(node.right)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif and node.balanceFactor > 0:
            if node.left and node.left.balanceFactor < 0:
                self.rotateLeft(node.left)
                self.rotateRight(node)
            else:
                self.rotateRight(node)



class TestAVL(unittest.TestCase):
    def setUp(self):
        self.avl = AVL()
        array = [(9, "A"), (3, "B"), (5, "C"), (11, "D"), (15, "E"), (2, "F"),
                (14, "G"), (18, "H")]
        for tup in array:
            self.avl.put(tup[0], tup[1])

    def test_put(self):
        result = self.avl.size
        self.assertEqual(result, 8)

    # def test_updateBalance(self):
    #     new_tup = (23, "Z")


if __name__ == "__main__":
    unittest.main()
