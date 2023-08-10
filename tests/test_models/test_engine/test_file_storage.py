#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    '''TestFileStorage Class'''

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

    def test_new_with_different_objects(self):
        '''Test that new method can handle different types of objects'''
        class DummyClass:
            pass

        dummy_obj = DummyClass()
        with self.assertRaises(AttributeError):
            self.storage.new(dummy_obj)

    def test_save_creates_file(self):
        '''Test that save method creates file if it doesn't exist'''
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage.save()  # Fixed here
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload_with_nonexistent_file(self):
        '''Test that reload method handles nonexistent file'''
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        # Should not raise an exception
        self.storage.reload()  # Fixed here

    def test_reload_with_corrupted_json(self):
        '''Test that reload method handles corrupted JSON file'''
        with open(self.file_path, 'w') as file:
            file.write("This is not valid JSON content")
        # Should not raise an exception
        self.storage.reload()  # Fixed here


if __name__ == "__main__":
    unittest.main()
