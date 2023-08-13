#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        SetUp testing User
        '''
        self.my_user = User()
        self.my_user.email = "user@example.com"
        self.my_user.password = "password123"
        self.my_user.first_name = "John"
        self.my_user.last_name = "Doe"

    def test_initialization(self):
        self.assertTrue(isinstance(self.my_user, BaseModel))
        self.assertTrue(hasattr(self.my_user, 'id'))
        self.assertTrue(hasattr(self.my_user, 'created_at'))
        self.assertTrue(hasattr(self.my_user, 'updated_at'))
        self.assertEqual(type(self.my_user.id), str)
        self.assertEqual(type(self.my_user.created_at), datetime)

    def test_string_representation(self):
        user_str = str(self.my_user)
        self.assertIn(self.my_user.__class__.__name__, user_str)
        self.assertIn(self.my_user.id, user_str)
        self.assertIn(str(self.my_user.__dict__), user_str)

    def test_save_method(self):
        updated_at = self.my_user.updated_at
        self.my_user.save()
        self.assertNotEqual(updated_at, self.my_user.updated_at)

    def test_to_dict_method(self):
        user_dict = self.my_user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)

    def test_custom_attributes(self):
        self.assertEqual(self.my_user.email, "user@example.com")
        self.assertEqual(self.my_user.password, "password123")
        self.assertEqual(self.my_user.first_name, "John")
        self.assertEqual(self.my_user.last_name, "Doe")

if __name__ == '__main__':
    unittest.main()
