#!/usr/bin/python3
'''
Module that define BaseModel class
'''
import uuid
from datetime import datetime


class BaseModel:
    '''
    BaseModel:
        class that defines all common attributes/methods for other classes
    '''
    def __init__(self):
        '''
        Initialization of the base model
        '''
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        '''
        Public instance attributes:
        return the string representation of:
        [<class name>] (<self.id>) <self.__dict__>
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        Public instance methods: updates the public instance attribute
        "updated_at" with the current datetime
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        Public instance methods:
        dictionary containing all keys/values of __dict__ of the instance
        '''
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
