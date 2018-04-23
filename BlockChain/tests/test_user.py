import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user1 = User('Alice')
        self.user2 = User('Bob')

    def test_creation(self):
        publicKey_Alice = self.user1.publicKey
        address_Alice = self.user1.address
        self.assertEqual(type(publicKey_Alice), str)
        self.assertEqual(len(address_Alice), 64)
