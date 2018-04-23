import unittest
import queue
import pdb
from enum import Enum

class Color(Enum):
    White = 0
    Gray = 0.5
    Black = 1

class Vertex():
    def __init__(self, key):
        self._id = key
        self._connectedTo = {}
        self.color = Color.White
        self.incoming = 0

    def addNeighbour(self, nbr, weight=0):
        self._connectedTo[nbr] = weight

    def getWeight(self, key):
        return self._connectedTo[nbr]

    def __lt__(self, other):
        return self.incoming < other.incoming

    @property
    def connectedTo(self):
        return self._connectedTo

    @property
    def id(self):
        return self._id

    def __str__(self):
        return str(self._id) + ' connectedTo: ' + str([conn._id for conn in self._connectedTo])

    def __repr__(self):
        return self.__str__()


class Graph():
    def __init__(self):
        self._vertList = {}
        self._numVertices = 0

    def addVertex(self, vertex):
        new_vertex = Vertex(vertex)
        self._vertList[vertex] = new_vertex
        self._numVertices += 1
        return new_vertex

    def getVertex(self, vertex):
        return self._vertList[vertex]

    def addEdge(self, vertexFrom, vertexTo, weight=0):
        if vertexFrom not in self._vertList:
            self.addVertex(vertexFrom)
        if vertexTo not in self._vertList:
            self.addVertex(vertexTo)
        self._vertList[vertexFrom].addNeighbour(self._vertList[vertexTo], weight)

    def bfs(self, vertex):
        q = queue.Queue()
        q.put(vertex)
        while not q.empty():
            currentVertex = q.get()
            self.visit(currentVertex)
            currentVertex.color = Color.Black
            for connection in currentVertex.connectedTo:
                if connection.color == Color.White:
                    q.put(connection)
                    connection.color = Color.Gray
                    connection.color = Color.Black

    def dfs(self, vertex):
        for connection in vertex.connectedTo:
            if connection.color == Color.White:
                connection.color = Color.Gray
                self.dfs(connection)
        self.visit(vertex)
        vertex.color = Color.Black

    def visit(self, vertex):
        print("Vertex being visited is: ", vertex)


    @property
    def vertList(self):
        return self._vertList

    @property
    def numVertices(self):
        return self._numVertices

    def __iter__(self):
        for key, value in self._vertList.items():
            yield value


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.g = Graph()
        graph = {
            0: [1, 4, 5],
            1: [3, 4],
            2: [1],
            3: [2, 4],
            4: [],
            5: []
        }
        for vertex, connections in graph.items():
            for edge in connections:
                self.g.addEdge(vertex, edge)

    def test_creation(self):
        self.assertEqual(self.g.numVertices, 6)

    def test_bfs(self):
        root = self.g._vertList[0]
        self.g.bfs(root)
        for vertex in self.g:
            self.assertEqual(vertex.color, Color.Black)

    def test_dfs(self):
        print('\n')
        root = self.g._vertList[0]
        self.g.dfs(root)
        for vertex in self.g:
            self.assertEqual(vertex.color, Color.Black)


if __name__ == "__main__":
    unittest.main()
