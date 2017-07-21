#! /usr/bin/env python3
import Employee
import Rank

class Manager(Employee):
    def __init__(self, callHandler):
        super().__init__(self, callHander)
        self.rank = Rank.MANAGER
