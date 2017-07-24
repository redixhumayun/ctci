#! /usr/bin/env python3
from enum import Enum

class Orientation(Enum):
    """
    A class to store the orientation of each piece
    Attributes:
    LEFT, TOP, RIGHT, BOTTOM
    """
    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3

    def __init__(self):
        pass

    def rotateClockWise(self):
        #need to replace with python equivalent of switch/case statements
        switch(self):
            case LEFT:
                return TOP
            case TOP:
                return RIGHT
            case RIGHT:
                return BOTTOM
            case BOTTOM:
                return TOP

    def getOpposite(self):
        #need to replace with python equivalent of switch/case statements
        switch(self):
        case LEFT:
            return RIGHT
        case RIGHT:
            return LEFT
        case TOP:
            return BOTTOM
        case BOTTOM:
            return TOP
