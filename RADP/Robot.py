#! /usr/bin/env python3
import pdb

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

def findPath(grid, row, column, pathArray, failedPoints):
    '''
    findPath is a function to help a robot move through a grid
    Return type: grid of path
    '''
    # pdb.set_trace()
    try:
        current = grid[row][column]
    except IndexError:
        return False#robot has stepped out of bounds

    point = Point(row, column) #creating point object here

    if point in failedPoints:
        return False

    if current == 2:
        #robot reached end
        return True
    if current == 0:
        #robot cannot go on this path
        failedPoints.append(point)
        return False

    pathArray.append(point)
    result = findPath(grid, row, column+1, pathArray, failedPoints) or \
            findPath(grid, row+1, column, pathArray, failedPoints)
    return result



if __name__ == "__main__":
    grid = [[1,1,0,1],[1,1,1,0],[1,0,1,1],[0,1,1,0], [1,1,1,0], [1,0,1,2]]
    #0 - robot cannot go on
    #1 - robot can go on
    #2 - end point

    pathArray = []
    failedPoints = []

    result = findPath(grid, 0, 0, pathArray, failedPoints)
    if result is True:
        print("Found path")
    else:
        print("Could not find path")
