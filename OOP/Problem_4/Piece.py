#! /usr/bin/env python3
import Orientation from Orientation

class Piece():
    """
    A class to instantiate piece of a jigsaw puzzle.
    Attributes:
    EdgeList: List of edges of the piece
    """

    def __init__(self, orientation):
        self.edgeList = [] #List of edges associated with the piece
        #should be in the order [TOP, RIGHT, BOTTOM, LEFT]

        self.orientation = orientation

    def getTopEdge(self):
        return self.edgeList[0]

    def getRightEdge(self):
        return self.edgeList[1]

    def getBottomEdge(self):
        return self.edgeList[2]

    def getBottomEdge(self):
        return self.edgeList[3]

    def getOrientations(self):
        #method to return all possible orientations of the piece
        orientations = {} #let orientations be in order TOP, RIGHT, BOT, LEFT
        for i, val in enumerate(self.edgeList):
            orientations[i] = self.edgeList
            self.rotateEdgeBy(1)
        return orientations

    def setOrientation(self, orientation):
        self.orientation = orientation

    def getEdgeWithOrientation(self, orientation):
        if orientation == Orientation.RIGHT:
            return self.edgeList[1] #returning right edge
        else:
            #returning bottom edge
            return self.edgeList[2]


    def findFlatEdges(self):
        #utility method to find number of flat edges
        flatCtr = 0
        for edge in self.edgeList:
            if edge.getShape() == FLAT:
                flatCtr += 1

    def isCorner(self):
        flatCtr = self.findFlatEdges()
        if flatCtr == 2:
            return True
        else:
            return False

    def isBorder(self):
        flatCtr = self.findFlatEdges()
        if flatCtr == 1:
            return True
        else:
            return False

    def rotateEdgeBy(self, numOfRot):
        for i in range(numOfRot):
            self.orientation = Orientation.rotateClockWise()
            self.rotateEdgeList() #rotate edgeList to match orientation

    def rotateEdgeList(self):
        self.edgeList[3:] + self.edgeList[:3]
