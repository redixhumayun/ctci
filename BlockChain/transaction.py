import hashlib

class Transaction():
    def __init__(self, refTrac, sen, senPrivateKey, rec, amount):
        #if refTrac is None, this is a coinbase transaction
        self.txid = refTrac #reference Transaction which serves as input
        self.sender = sen #public key of sender
        self.sender_privateKey = senPrivateKey #private key of sender
        self.recipient = recipient #public key of recipient
        self.amount = amount
        self.hash = self.buildHash()

    def buildHash(self):
        return hashlib.sha256(
                self.sender_privateKey + str(amount).encode('utf-8') + self.recipient)
                .hexdigest()
