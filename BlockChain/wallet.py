class Wallet():
    def __init__(self, address):
        self.address = address
        self.utxo = [] #list of unspent transaction outputs

    def incomingTransaction(self, transaction):
        self.utxo.append(transaction)
