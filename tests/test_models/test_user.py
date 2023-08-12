#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel
import datetime

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.email = "johndoe@example.com"
        self.user.password = "password123"

    def test_instance(self):
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertEqual(self.user.first_name, 'John')
        self.assertEqual(self.user.last_name, 'Doe')
        self.assertEqual(self.user.email, 'johndoe@example.com')
        self.assertEqual(self.user.password, 'password123')

    def test_id_generation(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_datetime_attributes(self):
        self.assertIsInstance(self.user.created_at, datetime.datetime)
        self.assertIsInstance(self.user.updated_at, datetime.datetime)

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['first_name'], 'John')
        self.assertEqual(user_dict['last_name'], 'Doe')
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
