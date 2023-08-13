#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
from models.user import User


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        '''
        SetUp method
        '''
        self.storage = FileStorage()
        self.my_model = BaseModel()
        self.my_user = User()
        self.my_user.email = "user@example.com"
        self.my_user.password = "password123"

    def tearDown(self):
        '''
        TearDown method
        '''
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_method(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        self.storage.new(self.my_model)
        self.assertIn('BaseModel.' + self.my_model.id, self.storage.all())

    def test_save_method(self):
        self.storage.new(self.my_model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_method(self):
        self.storage.new(self.my_model)
        self.storage.new(self.my_user)
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn('BaseModel.' + self.my_model.id, all_objects)
        self.assertIn('User.' + self.my_user.id, all_objects)

if __name__ == '__main__':
    unittest.main()
