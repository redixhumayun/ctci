import pdb

class BT():
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, key, node):
        # pdb.set_trace()
        if node is None:
            node = self.root

        if self.root is None:
            self.root = TreeNode(key)
            return self.root

        if key <= node.value:
            if node.left is None:
                node.left = TreeNode(key)
                return node.left
            else:
                return self.add(key, node.left)

        else:
            if node.right is None:
                node.right = TreeNode(key)
                return node.right
            else:
                return self.add(key, node.right)


    def getRankOfNumber(self, x, root):
        # pdb.set_trace()
        if root is None or root.value == x:
            return 0
        #add one to some counter
        return 1 + self.getRankOfNumber(x, root.left) + self.getRankOfNumber(x, root.right)


    def __repr__(self):
        return "The root of the tree is: " % self.root

class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self._track = None

    def insertLeftChild(self, value):
        self.left = value

    def insertRightChild(self, value):
        self.right = value

    @property
    def track(self):
        return self._track

    @track.setter
    def track(self, value):
        self._track = value #tracks the numbers of values less than this number

    def __repr__(self):
        return "Value is: %s" % self.value

class Stream():
    def __init__(self):
        self.values = [5,1,4,4,5,9,7,13,3]

    def __iter__(self):
        for value in self.values:
            yield value


if __name__ == "__main__":
    bt = BT()
    stream = Stream()
    for number in stream:
        node = bt.add(number, None)
        rank = bt.getRankOfNumber(number, bt.root)
        node.track = rank
