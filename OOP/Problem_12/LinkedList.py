#! /usr/bin/env python3
from Node import Node

class LinkedList():
    '''
    A class for the LinkedList instance to be used in HashTable.py
    Attributes: head
    '''

    def __init__(self):
        self.head = None

    def addNode(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.setNext(self.head)
            self.head = new_node

    def searchNode(self, value):
        curr = self.head
        while curr is not None:
            if curr.getValue() == value:
                return curr
            else:
                curr = curr.getNext()
        return None

    def deleteNode(self, value):
        curr = self.head
        prev = None
        found = False
        while curr is not None and found is False:
            if curr.getValue() == value:
                found = True
            else:
                prev = curr
                curr = curr.getNext()
        if found is False:
            raise ValueError("Node is not found")
        elif prev is None:
            self.head = curr.getNext()
        else:
            prev.setNext(curr.getNext())
