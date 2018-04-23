import seccure
import secrets
import hashlib
from wallet import Wallet

class User():
    def __init__(self, name):
        self.name = name
        self._privateKey = self.generatePrivateKey()
        self._publicKey = self.generatePublicKey()
        self._address = self.generateAddress()
        self.wallet = Wallet(self._address)

    @property
    def publicKey(self):
        return self._publicKey

    @property
    def address(self):
        return self._address

    def generatePrivateKey(self):
        return bytearray.fromhex(secrets.token_hex(64))

    def generatePublicKey(self):
        return str(seccure.passphrase_to_pubkey(self._privateKey))

    def generateAddress(self):
        return hashlib.sha256(self._publicKey.encode('utf-8')).hexdigest()
