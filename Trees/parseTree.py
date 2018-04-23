from BST import BinarySearchTree
from BST import TreeNode
import unittest
import pdb

class parseTree(BinarySearchTree):
    '''
    A class that will function as a parse tree.
    Inherits from the BST
    '''
    def __init__(self):
        super().__init__()

    def insert(self, value, node):
        # pdb.set_trace()
        if value == '(':
            node.left = TreeNode(0, 0)
            node.left.parent = node
            return node.left
        if value == ')':
            if node.parent:
                return node.parent
            else:
                return node
        if value not in ['+', '-', '*', '/']:
            #value is a number
            node.value = value
            return node.parent
        if value in ['+', '-', '*', '/']:
            #value is an expression
            node.value = value
            node.right = TreeNode(0, 0)
            node.right.parent = node
            return node.right

    def evaluate(self, root):
        if root is None:
            return
        if root.isLeaf():
            return root.value
        leftValue = self.evaluate(root.left)
        operand = root.value
        rightValue =  self.evaluate(root.right)
        return self.evaluateExpression(operand, leftValue, rightValue)

    def evaluateExpression(self, operand, left, right):
        if operand == '+':
            return int(left) + int(right)
        if operand == '-':
            return int(left) - int(right)
        if operand == '*':
            return int(left) * int(right)
        if operand == '/':
            return int(left) / int(right)



class TestParseTree(unittest.TestCase):
    def setUp(self):
        exp = "( 3 + ( 4 * 5 ) )"
        exp = exp.split(' ')
        self.pt = parseTree()
        self.pt.root = TreeNode(0, 0)
        self.node = self.pt.root
        for i in exp:
            self.node = self.pt.insert(i, self.node)

    def test_insert(self):
        self.assertEqual(self.node.value, '+')

    def test_evaluate(self):
        result = self.pt.evaluate(self.node)
        self.assertEqual(result, 23)

    def test_evaluateExpression(self):
        a = 5
        b = 3
        operand = '+'
        result = self.pt.evaluateExpression(operand, a, b)
        self.assertEqual(result, 8)


if __name__ == "__main__":
    unittest.main()
