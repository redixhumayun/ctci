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
            return

        if key <= node.value:
            if node.left is None:
                node.left = TreeNode(key)
                return
            else:
                self.add(key, node.left)
            node.left_size += 1

        else:
            if node.right is None:
                node.right = TreeNode(key)
                return
            else:
                self.add(key, node.right)


    def __repr__(self):
        return "The root of the tree is: " % self.root

class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self._track = None
        self.left_size = 0

    def insertLeftChild(self, value):
        self.left = value

    def insertRightChild(self, value):
        self.right = value

    #this method needs to be called on the root initially
    def getRankOfNode(self, v): #v needs to be value we are looking for
        # pdb.set_trace()
        if self.value == v:
            return self.left_size
        elif v < self.value:
            if self.left is None:
                return -1
            else:
                self.left.getRankOfNode(v)
        else:
            if self.right is None:
                return -1
            else:
                return self.left_size + 1 + self.right.getRankOfNode(v)


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
        bt.add(number, None)
    result = bt.root.getRankOfNode(9)
    print(result)
