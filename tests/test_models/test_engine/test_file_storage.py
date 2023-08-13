#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
import os
import models


class FileStorageTestCase(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_empty_all(self):
        all_objects = self.storage.all()
        self.assertEqual(all_objects, {})

    def test_new_with_base_model(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn('BaseModel.' + obj.id, self.storage.all())

    def test_save_and_reload_with_multiple_objects(self):
        obj1 = User()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertIn('User.' + obj1.id, all_objects)
        self.assertIn('BaseModel.' + obj2.id, all_objects)

    def test_new_without_saving(self):
        obj = User()
        new_storage = FileStorage()
        self.assertIn('User.' + obj.id, new_storage.all())

    def test_reload_without_file(self):
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIsInstance(new_storage.all(), dict)

    def test_save_with_existing_file(self):
        obj = User()
        self.storage.new(obj)
        self.storage.save()
        self.storage.save() # Save again
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_with_nonexistent_class(self):
        obj_dict = {"NonexistentClass.id": {"__class__": "NonexistentClass"}}
        with open("file.json", 'w') as file:
            file.write(str(obj_dict))
        self.storage.reload()
        self.assertNotIn('NonexistentClass.id', self.storage.all()) # Check for absence of specific key

if __name__ == '__main__':
    unittest.main()
