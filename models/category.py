#!/usr/bin/env python3
'''This module defines a catergory class'''
from models.base_model import BaseModel


class Category(BaseModel):
    '''Defines a category class '''
    name = ''
    item_id = []
    description = ''
