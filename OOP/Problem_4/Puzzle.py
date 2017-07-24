#! /usr/bin/env python3
import Orienation from Orientation

class Puzzle():
    """
    A class to store the puzzle. This will store the list of all pieces
    Attributes:
    pieces: List of pieces
    solution: NxN dimensional array (rows x columns)
    """

    def __init__(self, pieces, size):
        self.pieces = pieces #list of overall pieces
        self.cornerPieces = [] #list of corner pieces
        self.borderPieces = [] #list of border pieces
        self.innerPieces = [] #list of inner pieces
        self.size = size
        self.solution = [[0 for x in range(size)]for y in range(size)]

    def setEdgeInSolution(self, piece, orientation, row, column):
        piece.orientation = orientation
        self.solution[row][column] = piece
        self.pieces.remove(piece)

    def groupPieces(self):
        #method to group pieces
        for piece in self.pieces:
            if piece.isCorner():
                self.cornerPieces.append(piece)
            elif piece.isBorder():
                self.borderPieces.append(piece)
            else:
                self.innerPieces.append(piece)

    def isBorderIndex(self, index):
        if index == 0 or index == size - 1:
            return True
        else:
            return False

    def getPieceSearchList(self, row, col):
        if self.isBorderIndex(row) and self.isBorderIndex(col):
            return self.cornerPieces
        elif self.BorderIndex(row) or self.isBorderIndex(col):
            return self.edgePieces
        else:
            return self.innerPieces

    def orientTopLeftCorner(self, p):
        #method to identify top left corner of puzzle and place it
        orientations = p.getOrientations()
        for key, orientation in orientations.items():
            #orientation is stored as TOP, RIGHT, BOTTOM, LEFT
            if orientation[0] == 0 and orientation[3] == 0:
                p.setOrientation(key)
                return

    def fitNextEdge(self, searchList, row, col):
        if row == 0 and col == 0:
            p = searchList[0]
            del searchList[0]
            self.orientTopLeftCorner(p)
            self.solution[0][0] = p
        else:
            pieceToMatch = if col == 0 self.solution[row-1][0] else self.solution[row][col-1]
            orientationToMatch = if col == 0 Orientation.BOTTOM else Orientation.RIGHT
            edgeToMatch = pieceToMatch.getEdgeWithOrientation(orientationToMatch)
            #get opposite of the edge and check for a piece with that edge in
            #the correct orientation

    def solve(self):
        #start solution by grouping pieces
        self.groupPieces()
        for row in range(size):
            for col in range(size):
                pieceSearchList = self.getPieceSearchList(row, col)
                self.fitNextEdge(pieceSearchList, row, col)
