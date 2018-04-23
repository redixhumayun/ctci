class Network():
    '''
    A class that will house a dict of names along with wallet addresses of
    members of the network for easy lookup
    '''

    def __init__(self):
        self.lookupTable = {}

    def sendFundsToUser(self, addToSend):
        for name, add in self.lookupTable.items():
            if add == addToSend:
                addToSend.incomingTransaction()

    def addMember(self, name, wallet): #let wallet_add be instance of wallet
        if name not in self.lookupTable:
            self.lookupTable[name] = [wallet]
        else:
            self.lookupTable[name].append(wallet)

    def removeMember(self, name):
        if name in self.lookupTable:
            self.lookupTable.pop(name, None)
        else:
            print("Member not found in network.")
