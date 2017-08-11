import pdb

def queenAttack(n, k, rQueen, cQueen):
    rQueen = n - rQueen
    cQueen = cQueen - 1
    count = initialCount(n, rQueen, cQueen)
    return count

def addObstacle(n, count, rQueen, cQueen, rObstacle, cObstacle):
    rObstacle = rObstacle - 1
    cObstacle = cObstacle - 1
    if rObstacle == rQueen:
        #they are in the same row
        if cObstacle < cQueen:
            count -= rObstacle + 1 #+1 to account for 0 indexing
        else:
            count -= (n - rObstacle)
    elif cObstacle == cQueen:
        #they are in the same column
        if rObstacle < rQueen: #obstacle is above queen
            count -= cObstacle + 1 #+1 to account for 0 indexing
        else:
            count -= (n - cObstacle)
    else:
        #they are in diagonals
        if rObstacle > rQueen:
            if cObstacle > cQueen: #bottom right
                count -= min(n - rObstacle, n - cObstacle)
            elif cObstacle < cQueen: #bottom left
                count -= min(n - rObstacle, cObstacle+1)
        else:
            if cObstacle > cQueen: #upper right
                count -= min(rObstacle + 1, n - cObstacle)
            elif cObstacle < cQueen: #upper left
                count -= min(rObstacle + 1, cObstacle + 1)
    return count


def initialCount(n, rQueen, cQueen):
    count = 0

    #count in row
    count += n - 1 #-1 for queen square
    #count in column
    count += n - 1

    #primary diagonal squares
    upper_left = min(rQueen, cQueen)
    bottom_right = min(n - (rQueen + 1), n - (cQueen + 1))
    primary_diagonal = upper_left + bottom_right
    count += primary_diagonal

    #secondary diagonal squares
    upper_right = min(rQueen, n - (cQueen + 1))
    bottom_left = min(n - (rQueen + 1), cQueen)
    secondary_diagonal = upper_right + bottom_left
    count += secondary_diagonal

    return count



if __name__ == "__main__":
    n = 5
    k = 3
    rQueen = 4
    cQueen = 3
    count = queenAttack(n, k, rQueen, cQueen)
    obstacles = [(5,5), (4,2), (2,3)]
    for obstacle in obstacles:
        pdb.set_trace()
        count = addObstacle(n, count, rQueen, cQueen, obstacle[0], obstacle[1])
    print(count)
