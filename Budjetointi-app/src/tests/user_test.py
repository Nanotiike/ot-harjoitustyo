import unittest
from user import User

class testUset(unittest.TestCase):
    def setUp(self):
        self.user = User("Mikko", "540")

    def test_user_is_set_up(self):
        self.assertEqual(self.user.name,"Mikko")
        self.assertEqual(self.user.password,"540")