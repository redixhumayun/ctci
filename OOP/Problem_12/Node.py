#! /usr/bin/env python3

class Node():
    '''
    A python class for the node object to be used in LinkedList
    '''

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def getValue(self):
        return self.value

    def setNext(self, nodeObj):
        self.next_node = nodeObj

    def getNext(self):
        return self.next_node
        
