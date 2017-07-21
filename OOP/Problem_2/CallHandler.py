#! /usr/bin/env python3
from abc import ABCMeta, abstractmethod
from random import random
import Call
import Respondent
import Manager
import Director

class CallHandler():
    """Class that will hold the main body of the function.
    All calls routed through this
    """
    LEVELS = 3
    NUM_RESPONDENTS = 10
    NUM_MANAGERS = 4
    NUM_DIRECTORS = 2
    employeeLevels = []
    callQueues = []

    def __init__(self):
        #adding the respondents here
        self.respondents = []
        for k in range(0, self.NUM_RESPONDENTS):
            self.respondents.append(Respondent())
        self.employeeLevels.append(self.respondents)

        #adding the managers here
        self.managers = []
        for k in range(0, self.NUM_MANAGERS):
            self.managers.append(Manager())
        self.employeeLevels.append(self.managers)

        #adding the director here
        self.directors = []
        for k in range(0, self.NUM_DIRECTORS):
            self.directors.append(Director())
        self.employeeLevels.append(self.directors)

    def getHandlerForCall(self, call):
        level = call.getRank().getValue()
        for l in range(level, LEVELS - 1):
            employeeLevel = self.employeeLevels[l]
            for emp in employeeLevel:
                if emp.isFree():
                    return emp

        return None

    def dispatchCall(self, caller):
        call = Call()
        self.dispatchNewCall(call)

    def dispatchNewCall(self, call):
        emp = getHandlerForCall(call)
        if emp is not None:
            emp.receiveCall()
            call.setHandler(emp)
        else:
            call.reply("Please wait")
            self.callQueues[call.getRank().getValue()].append(call)

    def assignCall(self, emp):
        #function to assign a new call to an employee
        rank = emp.getRank().getValue()
        for r in range(rank, -1):
            queue = self.callQueues[rank]
            if len(queue) > 0:
                call = queue.pop(0)
                if call is not None:
                    emp.receiveCall(call)
                    return True

        return False
