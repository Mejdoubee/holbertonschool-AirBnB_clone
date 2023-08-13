#!/usr/bin/python3
'''
Model that defines State class
'''
from models.base_model import BaseModel


class State(BaseModel):
    '''State class that inherits from BaseModel'''
    state_id = ""
    name = ""
