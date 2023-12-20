#!/usr/bin/env python3
'''this defines a class user'''
from models.base_model import BaseModel


class User(BaseModel):
    '''defines a user in the database'''
    first_name = ''
    last_name = ''
    password = ''
    email = ''
    item_id = ''
    sales_id = ''
