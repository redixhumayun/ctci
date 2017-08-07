import pdb
import timeit

def sortedMatrix(matrix, elemToFind):
    # pdb.set_trace()
    colIndex = columnSearch(matrix, matrix[0], elemToFind)
    rowIndex = rowSearch(matrix, colIndex, elemToFind)
    for index in range(rowIndex, len(matrix[0])):
        result = binarySearch(matrix[index], colIndex, len(matrix[index]) - 1, elemToFind)
        if result:
            return matrix[index][result]
    return None

def columnSearch(matrix, row, elemToFind):
    colIndex = 0
    while colIndex < len(row) and elemToFind > row[colIndex]:
        colIndex += 1
    colIndex -= 1 #roll one back
    return colIndex

def rowSearch(matrix, colIndex, elemToFind):
    for index, row in enumerate(matrix):
        if elemToFind >= row[colIndex] and elemToFind <= row[len(row) - 1]:
            return index

def binarySearch(row, low, high, elemToFind):
    while low <= high:
        mid = (low + high) // 2
        if row[mid] < elemToFind:
            low = mid + 1
        elif row[mid] > elemToFind:
            high = mid - 1
        else:
            return mid
    return None

def column(matrix, i):
    return [row[i] for row in matrix]

def timing():
    SETUP_CODE = '''
from __main__ import sortedMatrix
    '''
    TEST_CODE = '''
matrix = [[15, 20, 40, 85],
        [20, 35, 80, 95],
        [30, 55, 95, 105],
        [40, 80, 100, 120]]
sortedMatrix(matrix, 35)
    '''
    print(timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=1000))


if __name__ == "__main__":
    timing()
