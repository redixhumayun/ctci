#! /usr/bin/env python3
from abc import ABC, abstractmethod

class Cell(ABC):
    '''
    An abstract class for the cell object. BlankCell, BombCell,
    NumberedCell will inherit from this class
    '''

    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.column = col
        self.flag = False
        self.isClicked = False

    def getValue(self):
        return self.value

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column

    def changeFlagValue(self):
        self.flag = not self.flag

    def cellClicked(self):
        self.isClicked = not self.isClicked

    def incrementValue(self):
        try:
            self.value += 1
        except TypeError:
            pass

    def isBomb(self):
        if self.value == 'X':
            return True
        else:
            return False

    def isBlank(self):
        if self.value == 0:
            return True
        else:
            return False
