#!/usr/bin/env python3
'''this defines a class user'''
from models.base_model import BaseModel, Base


class User(BaseModel):
    '''defines a user in the database'''
    password = ''
    email = ''
    item_id = ''
    sales_id = ''
