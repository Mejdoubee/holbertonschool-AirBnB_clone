#!/usr/bin/python3
'''
Model defines file_storage class that serializes instances
to a JSON file and deserializes JSON file to instances
'''
from models.base_model import BaseModel
import json
import os


class FileStorage:
    '''
    Serializes instances to a JSON file and deserializes JSON file to instances
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Returns the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        Sets in __objects the obj with key <obj class name>.id
        '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        '''
        Serializes __objects to the JSON file
        '''
        json_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(json_dict, f)

    def reload(self):
        '''
        Deserializes the JSON file to __objects
        '''
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)
                self.__objects = {}
                class_map = {'BaseModel': BaseModel}
                for key, value in json_objects.items():
                    class_name = value["__class__"]
                    obj_class = class_map.get(class_name)
                    if obj_class:
                        obj = obj_class(**value)
                        self.__objects[key] = obj

