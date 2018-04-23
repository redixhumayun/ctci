class Block():
    def __init__(self, transactions, parent):
        self.transactions = transactions
        self.verifiedTransactions = self.verifyTransactions()
        self.txnCount = len(self.verifiedTransactions)
        self.parent = parent

    def verifyTransactions(self):
        verifiedTransList = [] #O(n) space
        for transaction in self.transactions:
            if transaction.amount <= transaction.sender.balance:
                verifiedTransList.append(transaction)
            else:
                print("This transaction could not be processed: %s\n" % str(transaction.hash));
        return verifiedTransList

    def completeTransactions(self):
        for transaction in self.verifiedTransactions:
            transaction.sender.balance -= transaction.amount
            transaction.recipient.balance += transaction.amount
        print("Completed all transactions in this block")


class GenesisBlock(Block):
     def __init__(self, transactions):
         super().__init__(transactions, parent=None)
