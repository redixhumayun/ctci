import unittest
import pdb

class MazeSolution():
    '''
    A class representing the maze and its solution
    '''

    def __init__(self, maze, startPosition):
        self.maze = maze
        self.row, self.col = startPosition

    def searchFrom(self, row, col):
        if self.hitWall(row, col):
            return False
        if self.alreadyExplored(row, col):
            return False
        if self.outOfBounds(row, col):
            return False
        if self.isDeadEnd(row, col):
            return False
        if self.foundExit(row, col):
            self.maze[row][col] = 'P';
            return True
        self.maze[row][col] = '1'

        #go north here
        found = self.searchFrom(row-1, col)
        #go south here
        found = self.searchFrom(row+1, col)
        #go west here
        found = self.searchFrom(row, col-1)
        #go east here
        found = self.searchFrom(row, col+1)
        return found

    def isDeadEnd(self, row, col):
        if self.maze[row][col] == "D":
            return True
        return False

    def outOfBounds(self, row, col):
        try:
            self.maze[row][col]
        except IndexError:
            return True
        return False

    def alreadyExplored(self, row, col):
        if self.maze[row][col] == '1':
            return True
        return False

    def hitWall(self, row, col):
        if self.maze[row][col] == '+':
            return True
        return False

    def foundExit(self, row, col):
        if self.maze[row][col] == ' ':
            if row == 0 or row == len(self.maze) - 1:
                return True
            elif col == 0 or col == len(self.maze[0]) - 1:
                return True
        return False


class TestMazeSolution(unittest.TestCase):
    def setUp(self):
        self.maze = [['+','+','+','+','+','+','+','+','+','+','+'],
         ['+',' ',' ',' ',' ',' ',' ','+',' ',' ',' '],
         ['+',' ','+',' ','+','+',' ','+',' ','+','+'],
         ['+',' ','+',' ',' ',' ',' ','+',' ','+','+'],
         ['+','+','+',' ','+','+',' ','+',' ',' ','+'],
         ['+',' ',' ',' ','+','+',' ',' ',' ',' ','+'],
         ['+','+','+','+','+','+','+','+','+',' ','+'],
         ['+',' ',' ',' ','+','+',' ',' ','+',' ','+'],
         ['+',' ','+','+',' ',' ','+',' ',' ',' ','+'],
         ['+',' ',' ',' ',' ',' ','+',' ','+','+','+'],
         ['+','+','+','+','+','+','+',' ','+','+','+']]

        self.startPosition = (3,1)
        self.mazeClass = MazeSolution(self.maze, self.startPosition)

    def test_initilization(self):
        result = len(self.mazeClass.maze)
        self.assertEqual(result, 11)

    def test_isDeadEnd(self):
        self.mazeClass.maze[4][5] = 'D'
        self.assertEqual(self.mazeClass.isDeadEnd(4, 5), True)

    def test_outOfBounds(self):
        result = self.mazeClass.outOfBounds(14, 14)
        self.assertEqual(result, True)

    def test_foundExit(self):
        result = self.mazeClass.foundExit(1, 10)
        self.assertEqual(result, True)

    def test_solution(self):
        row, col = self.startPosition
        result = self.mazeClass.searchFrom(row, col)
        for row in self.mazeClass.maze:
            print(row)
        print(result)

if __name__ == "__main__":
    unittest.main()
