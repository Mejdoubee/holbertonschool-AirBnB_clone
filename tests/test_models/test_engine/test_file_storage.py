#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

class TestFileStorage(unittest.TestCase):
    
    def setUp(self):
        '''Set up method for FileStorage tests'''
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.file_path = "file.json"

    def test_file_path(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_all(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.storage.new(self.base_model)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        self.storage.save()
        os.remove(self.file_path)
        self.assertFalse(os.path.exists(self.file_path))
        new_storage = FileStorage()
        new_storage.reload()
        all_objects = new_storage.all()
        self.assertIsInstance(all_objects, dict)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

if __name__ == "__main__":
    unittest.main()
