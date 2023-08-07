#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        '''
        SetUp testing
        '''
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_initialization(self):
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))
        self.assertEqual(type(self.my_model.id), str)
        self.assertEqual(type(self.my_model.created_at), datetime)

    def test_string_representation(self):
        model_str = str(self.my_model)
        self.assertIn(self.my_model.__class__.__name__, model_str)
        self.assertIn(self.my_model.id, model_str)
        self.assertIn(str(self.my_model.__dict__), model_str)

    def test_save_method(self):
        updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(updated_at, self.my_model.updated_at)

    def test_to_dict_method(self):
        model_dict = self.my_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_custom_attributes(self):
        self.assertEqual(self.my_model.name, "My First Model")
        self.assertEqual(self.my_model.my_number, 89)


if __name__ == '__main__':
    unittest.main()
