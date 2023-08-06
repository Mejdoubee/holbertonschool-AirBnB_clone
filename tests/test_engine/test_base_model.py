#!/usr/bin/python3
'''
Unitest for BaseModel class
'''
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''
    Class TestBaseModel for BaseModel test cases
    '''

    def Test_Setup(self):
        '''
        SetUp testing
        '''
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def Test_Attributes(self):
        '''
        Attributes Testing
        '''
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))
        self.assertEqual(type(self.my_model.id), str)

    def Test_save_method(self):
        '''
        Save method Testhing
        '''
        old_update_time = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old_update_time)

    def test_to_dict_method(self):
        '''
        To_dict_method testing
        '''
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        model_dict = self.my_model.to_dict()
        self.assertEqual(model_dict["name"], "My First Model")


if __name__ == "__main__":
    unittest.main()
