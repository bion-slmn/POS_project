#!/usr/bin/env python3
'''This module defines a catergory class'''
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, DateTime, Column, Integer, String

class Category(BaseModel):
    '''Defines a category class '''

    __tablename__ = 'category'
    item_id = # relationship
    description = ''
