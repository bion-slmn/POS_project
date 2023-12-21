#!/usr/bin/env python3
'''this defines a class item'''
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, DateTime, Column, Float, String


class Item(BaseModel, Base):
    '''defines a class item describes how items sold
    are defined'''

    __tablename__ = "item"
    name = Column(String(120), unique=True, nullable=False)
    buying_price = Column(Float, nullable=False)
    selling_price = Column(Float,  nullable=False)
    photo = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    category_id = # foregin Key
