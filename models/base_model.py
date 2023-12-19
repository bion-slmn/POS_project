#!/usr/bin/env python3
'''This module defines a base model class '''
import uuid


class BaseModel:
    ''' this model is the parent of all other classes
     its in herited by all models'''

    def __init__(self, **kwargs):
        '''this method intialises the parameters '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dict(self):
        '''this method return a dictionary version of the class'''
        new_dict = self.__dict__.copy()
        new_dict.pop('_sa_instance_state', None)

        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    def save(self):
        '''saving an item to the database'''
        storage.new(self)
        storage.save()

    def delete(self):
        '''deletes an object from the storage'''
        storage.delete(self)
