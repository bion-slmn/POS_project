#!/usr/bin/env python3
'''This module defines a catergory class'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Text
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    '''Defines a category class '''

    __tablename__ = 'categories'
    items = relationship(
            'Item', backref='category', lazy='dynamic')
    description = Column(Text)
