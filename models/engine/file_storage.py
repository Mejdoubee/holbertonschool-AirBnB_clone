#!/usr/bin/python3
'''
Model defines file_storage class that serializes instances
to a JSON file and deserializes JSON file to instances
'''
import json
from models.base_model import BaseModel


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
        with open(self.__file_path, 'w') as f:
            json.dump(
                {key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        '''
        Deserializes the JSON file to __objects
        '''
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)

            class_mapping = {}
            for name, obj in globals().items():
                if isinstance(obj, type):
                    class_mapping[name] = obj

            for val in obj_dict.values():
                class_name = val.pop("__class__", None)
                if class_name:
                    class_instance = class_mapping.get(class_name)
                    if class_instance:
                        obj = class_instance(**val)
                        self.new(obj)

        except FileNotFoundError:
            return
