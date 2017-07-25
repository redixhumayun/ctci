#! usr/bin/env python3
import random
from BombCell import BombCell
from BlankCell import BlankCell

class Minesweeper():
    '''
    A class for the main game. This will instantiate the game and execute
    all controls of the game
    Attributes:
    Board: Double nested array that will hold the N*N game state
    CellList: List of all cells, with each being an object
    CellsPicked: List of all cells picked so far (clicked on)
    CellsShown: List of all cells that are shown to the user
    '''
    def __init__(self, size):
        self.cellsShown = [] #list to add the cells shown to the user
        self.size = size #size of the board. Will be size*size
        self.board = [0 for x in range(size) [for y in range(size)]]


    def startGame(self):
        #method to initialize the board
        self.placeBombs()

    def placeBombs(self):
        #Use fisher-yates algorithm to place bombs
        for row in range(self.size-1, 0, -1):
            elem = random.randint(0, row)
            for col in range(self.size-1, 0, -1):
                elem2 = random.randint(0, col)
                self.board[row][col] = BombCell(row, col)
                break

    def calculateCellValues(self):
        for row in range(size):
            for col in range(size):
                if self.board[row][col] == []:
                    self.board[row][col] = BlankCell(row, col)
                elif self.board[row][col].isBomb():
                    self.calculateSurroundingCellValues(row, col)

    def calculateSurroundingCellValues(self, row, col):
        for x in range(row - 1, row + 1):
            for y in range(col - 1, col + 1):
                if x != row and y != col:
                    self.board[row][col].incrementValue()

############################################################
#Initialization of the game done upto this point
############################################################

    def clickCell(self, row, col):

        cell = self.board[row][col]
        cell.cellClicked() #show cell as clicked
        cellsShown.append(cell) #add to cellsShown list

        if cell.isBlank():
            self.expandSurroundingCells(cell)
        elif cell.isBomb():
            #TODO Show whole board
            self.gameOver()
        #TODO Method to show all clicked cells throughout board

    def expandSurroundingCells(self, cell):
        #method to expand surrounding cells around a blank cell
        blankCellQueue = []
        blankCellQueue.append(cell)

        while len(blankCellQueue) > 0:
            cellToVisit = blankCellQueue.pop(0)

            row = cellToVisit.getRow()
            col = cellToVisit.getColumn()

            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if i != row and j != col:
                        if is self.board[i][j].isBlank():
                            blankCellQueue.append(self.board[i][j])
                        else:
                            self.showCell(self.board[i][j])

    def showCell(cell):
        cell.cellClicked()
        cellsShown.append(cell)

    def gameOver(self):
        print("Oops! Game over")
