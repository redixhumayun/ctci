#! /usr/bin/env python3
import pdb

def EightQueens(board, row, col, results):
    '''
    A method to solve the enigmatic eight queens problem
    Lessduet
    '''
    pdb.set_trace()
    if row < 0 or col < 0:
        results.append(board)
        return
    else:
        for i in range(col, 8, 1): #i represents the current column
            if(checkValid(board, row, i)):
                board[row][i] = i #value will be col where queen is placed
                                    #in that specific row
                EightQueens(board, row-1, col, results)


def checkValid(board, row, col):
    #Check each row for the same column.
    #Columns are already being iterated over in the previous EightQueens function
    for row2 in range(row, 8, 1):
        if board[row2][col] != 0:
            return False
    #After reaching this point, we know this column is empty.
    #col will be column of first empty cell in row

    #Need to find location of queen in next row
    #queenLocation will be column number
    queenLocation = findQueenInNextRow(board, row+1)
    colDistance = abs(queenLocation - col)
    if colDistance == 1:
        return False
    return True

def findQueenInNextRow(board, row):
    #check this whole row for the queen
    for col in range(0, 8, 1):
        if board[row][col] != 0:
            return col






def refreshBoard():
    return [[0 for y in range(8)]for x in range(8)]

if __name__ == "__main__":
    board = refreshBoard()
    result = EightQueens(board, 7, 0, [])
    print(result)
