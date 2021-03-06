#! /usr/bin/env python3
from Rank import Rank
from Caller import Caller

class Call():
    """
    A class representing a call from a customer
    """
    rank = None
    handler = None

    def __init__(self, c):
        self.rank = Rank.RESPONDENT
        self.caller = c

    def setHandler(self, emp):
        self.handler = emp

    def reply(self, message):
        print(message)

    def getRank(self):
        return self.rank

    def setRank(self, r):
        self.rank = r

    def incrementRank(self):
        if self.rank == Rank.RESPONDENT:
            self.rank = Rank.MANAGER
        elif self.rank == Rank.MANAGER:
            self.rank = Rank.DIRECTOR

        return self.rank

    def disconnect(self):
        print("Thank you for calling")
