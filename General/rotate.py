def rotate(m):
    #return [[m[j][i] for j in range(len(m) - 1, -1, -1)] for i in range(len(m[0]))]
    return [[row[i] for row in m] for i in range(len(m[0]))]


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
result = rotate(matrix)
print(result)
