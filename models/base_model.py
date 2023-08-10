#!/usr/bin/python3
'''
Model that defines BaseModel class
'''
import uuid
from datetime import datetime


class BaseModel:
    '''
    This class defines all common attributes/methods for other classes
    '''
    def __init__(self, *args, **kwargs):
        '''
        Initialization of the base model
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f"
                        )
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            from . import storage
            storage.new(self)

    def __str__(self):
        '''
        Return the string representation of:
        [<class name>] (<self.id>) <self.__dict__>
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        Updates the public instance attribute
        "updated_at" with the current datetime
        '''
        self.updated_at = datetime.now()
        from . import storage
        storage.save()

    def to_dict(self):
        '''
        Return a dictionary containing all
        keys/values of __dict__ of the instance
        '''
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
