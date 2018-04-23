from graph import Graph, Vertex
import pdb
import unittest
import heapq
from collections import deque

def TopologicalSort(graph):
    setIncoming(graph)

    pq = createQueue(graph)
    final_order = deque()
    processNext = deque()
    processNext.append(heapq.heappop(pq))

    while len(processNext) > 0:
        currentVertex = processNext.popleft()
        if currentVertex.incoming == 0:
            final_order.append(currentVertex)
            decrementEdges(currentVertex)
            if len(pq) > 0:
                processNext.append(heapq.heappop(pq))
        else:
            heapq.heappush(pq, currentVertex)
            processNext.append(heapq.heappop(pq))

    return final_order

def getOrder(final_order):
    final_result = []
    while len(final_order) > 0:
        final_result.append(final_order.popleft()._id)
    return final_result

def decrementEdges(vertex):
    for v in vertex.connectedTo:
        v.incoming -= 1


def createQueue(graph):
    pq = [] #priority queue
    for vertex, vertex_Obj in graph.vertList.items():
        heapq.heappush(pq, vertex_Obj)
    return pq

def setIncoming(graph):
    for vertex, vertex_Obj in graph.vertList.items():
        for connection in vertex_Obj.connectedTo:
            connection.incoming += 1

class TestTopSort(unittest.TestCase):
    def setUp(self):
        self.g = Graph()
        graph = {
            0: [],
            1: [],
            2: [3],
            3: [1],
            4: [0, 1],
            5: [0, 2]
        }

        for vertex, connections in graph.items():
            for edge in connections:
                self.g.addEdge(vertex, edge)

    def test_setIncoming(self):
        setIncoming(self.g)
        self.assertEqual(self.g.vertList[0].incoming, 2)
        self.assertEqual(self.g.vertList[1].incoming, 2)
        self.assertEqual(self.g.vertList[4].incoming, 0)

    def test_createQueue(self):
        result = createQueue(self.g)
        self.assertEqual(len(result), self.g.numVertices)

    def test_topologicalSort(self):
        final = getOrder(TopologicalSort(self.g))
        self.assertEqual(len(final), self.g.numVertices)
        self.assertEqual(final, [4, 5, 0, 2, 3, 1])

if __name__ == "__main__":
    unittest.main()
