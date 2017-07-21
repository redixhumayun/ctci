#! /usr/bin/env python3
import Employee
import Rank

class Respondent(Employee):
    def __init__(self, callHandler):
        super().__init__(self, callHandler)
        self.rank = Rank.RESPONDENT
