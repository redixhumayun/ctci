#! /usr/bin/env python3
from Employee import Employee
from Rank import Rank

class Manager(Employee):
    def __init__(self, callHandler):
        super().__init__(callHandler)
        self.rank = Rank.MANAGER
