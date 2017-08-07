import pdb

class Coordinate():
    matrix = [[15, 20, 40, 85], [20, 35, 80, 95], [30, 55, 95, 105], [40, 80, 100, 120]]
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def inbounds(self):
        checkRow = self.row >= 0 and self.row < len(matrix)
        checkCol = self.col >= 0 and self.col < len(matrix[0])
        return checkRow and checkCol

    def clone(self):
        return Coordinate(self.row, self.col)

    def isBefore(self, p):
        return self.row <= p.row and self.col <= p.col

    def setToAverage(self, minimum, maximum):
        self.row = (minimum.row + maximum.row) // 2
        self.col = (minimum.col + maximum.col) // 2

    def __repr__(self):
        return "row: %s, col: %s, value: %s" % (str(self.row), str(self.col), str(matrix[self.row][self.col]))

def findElement(matrix, origin, dest, elemToFind):
    pdb.set_trace()
    if not origin.inbounds() or not dest.inbounds():
        return None
    if matrix[origin.row][origin.col] == elemToFind:
        return origin

    start = origin.clone()
    diagDist = min(dest.row - origin.row, dest.col - origin.col)
    end = Coordinate(origin.row + diagDist, origin.col + diagDist)
    point = Coordinate(0, 0)

    while(start.isBefore(end)):
        point.setToAverage(start, end)
        if elemToFind > matrix[point.row][point.col]:
            start.row = point.row + 1
            start.col = point.col + 1
        else:
            end.row = point.row - 1
            end.col = point.col - 1

    return partitionAndSearch(matrix, origin, dest, start, elemToFind)

def partitionAndSearch(matrix, origin, dest, pivot, elemToFind):
    lowerLeftOrigin = Coordinate(pivot.row, origin.col)
    lowerLeftDest = Coordinate(dest.row, pivot.col - 1)
    upperRightOrigin = Coordinate(origin.row, pivot.col)
    upperRightDest = Coordinate(pivot.row - 1, dest.col)

    lowerLeft = findElement(matrix, lowerLeftOrigin, lowerLeftDest, elemToFind)
    if lowerLeft is None:
        return findElement(matrix, upperRightOrigin, upperRightDest, elemToFind)
    return lowerLeft

def sortedMatrix(matrix, elemToFind):
    origin = Coordinate(0, 0)
    dest = Coordinate(len(matrix) - 1, len(matrix[0]) - 1)
    return findElement(matrix, origin, dest, elemToFind)

if __name__ == "__main__":
    matrix = [[15, 20, 40, 85], [20, 35, 80, 95], [30, 55, 95, 105], [40, 80, 100, 120]]
    result = sortedMatrix(matrix, 85)
    print(result)
