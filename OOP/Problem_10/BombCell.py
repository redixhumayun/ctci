#! /usr/bin/env python3
from Cell import Cell

class BombCell(Cell):
    '''
    A class for the bomb cell. Will inherit from the main Cell class
    Attributes:
    '''

    def __init__(self):
        super().__init__('X') #bomb values will be 'X'
