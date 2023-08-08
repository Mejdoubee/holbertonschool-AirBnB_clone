#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models

class TestFileStorage(unittest.TestCase):
    
    def setUp(self):
        '''Set up method for FileStorage tests'''
        self.file_storage = FileStorage()
        self.base_model = BaseModel()
        self.file_path = "file.json"

    def test_all(self):
        '''Test that all method returns the correct dictionary'''
        all_objects = self.file_storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        '''Test that new method correctly adds an object to __objects'''
        key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.file_storage.new(self.base_model)
        self.assertIn(key, self.file_storage.all())

    def test_save(self):
        '''Test that save method correctly serializes objects to JSON file'''
        self.file_storage.save()
        with open(self.file_path, 'r') as file:
            self.assertTrue(file.read())

    def test_reload(self):
        '''Test that reload method correctly deserializes objects from JSON file'''
        self.file_storage.reload()
        all_objects = self.file_storage.all()
        self.assertIsInstance(all_objects, dict)
        # Add more specific checks to ensure that objects are correctly reloaded

    def tearDown(self):
        '''Clean up after tests'''
        import os
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

if __name__ == "__main__":
    unittest.main()
