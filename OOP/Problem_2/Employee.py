#! /usr/bin/env python3

class Employee():
    """
    An employee abstract class that will be inherited from by all employees
    """
    currentCall = None #variable to hold the current call here
    rank = None
    callHandler = None #variable to hold the instance of the CallHandler class

    def __init__(self, handler): #handler will be an instance of CallHandler
        self.callHandler = handler

    def receiveCall(self, call):
        #Assigning a call to an employee here
        print("receiving the call")
        self.currentCall = call

    def callCompleted(self):
        #checking if the call is completed for the employee
        if self.currentCall is not None:
            self.currentCall.disconnect()
            self.currentCall = None

        self.assignNewCall()

    def escalateAndResolve(self):
        if self.currentCall is not None:
            self.currentCall.incrementRank()
            self.callHandler.dispatchCall(self.currentCall)

            self.currentCall = None

        self.assignNewCall()

    def assignNewCall(self):
        if not self.isFree():
            return False
        else:
            return self.callHandler.assignCall()

    def isFree(self):
        return self.currentCall == None

    def getRank(self):
        return self.rank
