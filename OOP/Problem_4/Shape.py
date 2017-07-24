#! /usr/bin/env python3
from enum import Enum

class Shape(Enum):
    """
    A class to store information about edges of each piece
    Edge will have three possible types: INNER, OUTER, FLAT
    Each piece should have four edges
    """
    FLAT = 0
    INNER = 1
    OUTER = 2

    def __init__(self):
        pass
