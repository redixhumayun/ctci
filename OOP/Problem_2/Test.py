from CallHandler import CallHandler
from Caller import Caller

class Test():
    def __init__(self):
        self.ch = CallHandler()
        self.caller = Caller("Zaid", 21522632)
        self.ch.dispatchCall(self.caller)


if __name__ == "__main__":
    test = Test()
