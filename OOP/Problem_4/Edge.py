#! /usr/bin/env python3
from Shape import Shape

class Edge(Enum):
    """
    A class to store information about edges of each piece
    Edge will have three possible types: INNER, OUTER, FLAT
    Each piece should have four edges
    """
    def __init__(self, shape):
        self.shape = shape
        self.code = code #numeric value

    def getShape(self):
        return self.shape
