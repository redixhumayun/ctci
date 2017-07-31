def PaintFill(grid, r, c, old_col, new_col):
    '''
    A method to fill in all of the elements in a matrix
    '''
    try:
        grid[r][c]
    except IndexError:
        return
    if grid[r][c] == old_col:
        grid[r][c] = new_col
        PaintFill(grid, r-1, c, old_col, new_col) #up
        PaintFill(grid, r+1, c, old_col, new_col) #down
        PaintFill(grid, r, c-1, old_col, new_col) #left
        PaintFill(grid, r, c+1, old_col, new_col) #right
    return grid



if __name__ == "__main__":
    grid = [
        ['red','red','green'],
        ['green', 'green', 'green'],
        ['red', 'green', 'green']
    ]

    result = PaintFill(grid, 1, 1, 'green', 'red')
    print(result)
