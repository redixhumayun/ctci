def drawLine(screen, width, x1, x2, y):
    rowIndex = y * width #number of indexes per row = width, so finding correct row
    if x1 < 0 or x2 > 64:
        raise ValueError("Wrong indexes specified")
    ctrForPixel = 0
    start = round(x1 / 8) #pixel number at which to start drawing
    stop = round(x2 / 8) #pixel number at which to stop drawing
    for index in range(rowIndex, rowIndex + (start - stop) + 1, 1):
        #change current index to all 1s
        if screen[index] == 0:
            screen[index] = 1




if __name__ == "__main__":
    array = [0] * 64
    width = 8
    x1 = 15
    x2 = 45
    y = 2
