#! /usr/bin/env python3
from Cell import Cell

class NumberedCell(Cell):
    '''
    A class for the numbered cell. Will inherit from the main Cell class
    Attributes:
    '''

    def __init__(self, value):
        super().__init__(value) #numbered values will be provided
