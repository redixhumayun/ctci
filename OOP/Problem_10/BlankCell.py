#! /usr/bin/env python3
from Cell import Cell

class BlankCell(Cell):
    '''
    Class for blank cell. Inherits from Cell
    '''

    def __init__(self):
        super().__init__(0)
